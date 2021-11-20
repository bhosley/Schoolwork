import time

import cv2
import numpy as np
from pandas import DataFrame as DF
from stopwatch import Stopwatch

CAP = cv2.VideoCapture(0)
FONT = cv2.FONT_HERSHEY_SIMPLEX
KERNEL = np.ones((10, 10), np.uint8)
FIDUCIAL_THRESHOLD = 3000
MARKER_THRESHOLD = 1000
MARKER_RANGE = np.array([[0, 0, 255],[255, 255, 255]])

# Constants only for testing and dev purposes
trace_number = 5

#################
#   Functions   #
#################

def find_origin(frame):
    _x, _y, radius = 0, 0, 0
    for _ in range(100):     
        mask = cv2.inRange(frame, 
            np.array([0, 0, 0]),  # BGR Black
            np.array([75, 75, 75]))  # BGR lighter Black
        contours,h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            largest_contour = max(contours, key = cv2.contourArea) # Largest Contour
            area = cv2.contourArea(largest_contour)

            if area > FIDUCIAL_THRESHOLD:
                (cx, cy), r = cv2.minEnclosingCircle(largest_contour)
                _x += cx
                _y += cy
                radius += r

    # Tested 100 times, return average               
    center = (_x/100, _y/100)
    radius = radius/100
    return center, radius

#####################
#   Program Init    #
#####################

# Instantiate outside of loop variables
trace = []
mx, my = 0, 0
trace_x, trace_y = 0, 0
timer = Stopwatch()

# Determine reference frame
ret, frame = CAP.read()
origin, radius = find_origin(frame)

#####################
#   Program Loop    #
#####################

while True:
    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    _x, _y, c = 0, 0, 0
    for _ in range(3):  
        # Video capture and identify contours of potential markers
        ret, frame = CAP.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        marker_mask = cv2.inRange(hsv, MARKER_RANGE[0], MARKER_RANGE[1])
        marker_mask = cv2.dilate(marker_mask, KERNEL, iterations=1)
        contours,h = cv2.findContours(marker_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contours) > 0:
            largest_contour = max(contours, key = cv2.contourArea)
            area = cv2.contourArea(largest_contour)
    
            # If large enough, find coordinates of contour's moment 
            if area > MARKER_THRESHOLD:
                M = cv2.moments(largest_contour)
                _x += int(M["m10"] / M["m00"])
                _y += int(M["m01"] / M["m00"])
                c += 1

    if abs(_x) > 50 and abs(_y) > 50:
        # Marker coordinates are averaged of c successes of 100 attempts
        mx, my = _x/c, _y/c 
        
        # Normalize coordinates to fiducial radius
        trace_x, trace_y = (mx-origin[0])/radius, (origin[1]-my)/radius

        trace.append([timer.elapsed, trace_x, trace_y])
        
        # Start the timer after the first recorded marker
        if timer.elapsed == 0: 
            timer.start()
    
    # Sleep to prevent recording faster than 100 Hz;
    # We would like to avoid recording too many too small changes.
    #time.sleep(0.01) 

    # Output Image
    cv2.putText(frame,str('Marker: {},{}  Time: {}'.format(trace_x, trace_y, timer.elapsed)), (10,30), FONT, 1, (255,255,255), 2, cv2.LINE_AA)
    cv2.circle(frame, (int(origin[0]), int(origin[1])), 2, (0, 255, 0), 2)
    cv2.circle(frame, (int(origin[0]), int(origin[1])), int(radius), (255, 0, 0), 2)
    cv2.circle(frame, (int(mx), int(my)), 1, (0, 0, 255), 2)
    cv2.imshow('Detected Circles', frame)
    
    """     Testing items
    cv2.circle(mask, (int(mx), int(my)), 1, (0, 0, 255), 2)
    cv2.imshow('mask', marker_mask)
    if int(timer.elapsed) == 10:
        cv2.imwrite('../images/screen_cap{}.png'.format(trace_number), frame)
    """

####################
#   Program End    #
####################

# Convert trace data to dataframe and export as csv
export_data = DF(trace, columns = ['time', 'x', 'y'])
export_data.to_csv("./trace_{}.csv".format(trace_number), index=False)

# Kill view windows
CAP.release()
cv2.destroyAllWindows()