import cv2
import time
import numpy as np
from pandas import DataFrame as DF
from stopwatch import Stopwatch

CAP = cv2.VideoCapture(0)
FONT = cv2.FONT_HERSHEY_SIMPLEX
KERNEL = np.ones((10,10), np.uint8)
FIDUCIAL_THRESHOLD = 3000
MARKER_THRESHOLD = 500
MARKER_RANGE = np.array([[0, 0, 255],[255, 255, 255]])

# Constants only for testing and dev purposes
trace_number = 1

#################
#   Functions   #
#################

def find_origin(frame):
    x, y, radius = 0, 0, 0
    for _ in range(100):     
        mask = cv2.inRange(frame, 
            np.array([0, 0, 0]),  # BGR Black
            np.array([75, 75, 75]))  # BGR lighter Black
        contours,h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            largest_contour = max(contours, key = cv2.contourArea) # Largest Contour
            area = cv2.contourArea(largest_contour)

            if area > FIDUCIAL_THRESHOLD:
                (cx,cy),r = cv2.minEnclosingCircle(largest_contour)
                x += cx
                y += cy
                radius += r

    # Tested 100 times, return average               
    center = (x/100, y/100)
    radius = radius/100
    return center, radius

#####################
#   Program Init    #
#####################

# Instantiate outside of loop variables
trace = []
mx, my = 0, 0
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

    # Video capture and identify contours of potential markers
    ret, frame = CAP.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    marker_mask = cv2.inRange(hsv, MARKER_RANGE[0], MARKER_RANGE[1])
    marker_mask = cv2.dilate(marker_mask, KERNEL, iterations=2)
    contours,h = cv2.findContours(marker_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) > 0:
        largest_contour = max(contours, key = cv2.contourArea)
        area = cv2.contourArea(largest_contour)

        # If large enough, return coordinates of contour's moment 
        if area > MARKER_THRESHOLD:
            M = cv2.moments(largest_contour)
            mx = int(M["m10"] / M["m00"])
            my = int(M["m01"] / M["m00"])
            
            # Normalize coordinates to fiducial radius
            

            trace.append([timer, mx, my])
            
            # Start the timer after the first recorded marker
            if timer.elapsed == 0: timer.start()
    
    # Record no faster than 100 Hz;
    # We do not want to output too much data,
    # especially without enough time for relevant change.
    time.sleep(0.01) 

    # Output Image
    cv2.putText(frame,str('Marker: {},{}'.format(mx-origin[0], origin[1]-my)),(10,30), FONT, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.circle(frame, (int(origin[0]),int(origin[1])), 2, (0, 255, 0), 2)
    cv2.circle(frame, (int(origin[0]),int(origin[1])), int(radius), (255, 0, 0), 2)
    cv2.circle(frame, (int(mx),int(my)), 1, (0, 0, 255), 2)
    cv2.imshow('Detected Circles', frame)
    #cv2.imshow('Mask', marker_mask)

####################
#   Program End    #
####################

# Convert trace data to dataframe and export as csv
export_data = DF(trace, columns = ['time','x','y'])
export_data.to_csv("trace_{}.csv".format(trace_number),index=False)

# Kill windows
CAP.release()
cv2.destroyAllWindows()