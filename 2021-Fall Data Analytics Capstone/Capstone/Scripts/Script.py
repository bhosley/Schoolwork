import cv2
import numpy as np

CAP = cv2.VideoCapture(0)
FONT = cv2.FONT_HERSHEY_SIMPLEX
KERNEL = np.ones((10,10), np.uint8)
FIDUCIAL_THRESHOLD = 3000
MARKER_THRESHOLD = 500
MARKER_RANGE = np.array([[0, 0, 255],[255, 255, 255]])

# 
def find_origin(frame):
    x,y,radius = 0,0,0
    for _ in range(100):     
        mask = cv2.inRange(frame, 
            np.array([0, 0, 0]),  # BGR Black
            np.array([75, 75, 75]))  # BGR lighter Black

        contours,h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # Checking if any contour is detected then run the following statements
        if len(contours) > 0:
            cmax = max(contours, key = cv2.contourArea) # Largest Contour
            area = cv2.contourArea(cmax)
            if area > FIDUCIAL_THRESHOLD:
                (cx,cy),r = cv2.minEnclosingCircle(cmax)
                x += cx
                y += cy
                radius += r
                       
    center = (x/100, y/100)
    radius = radius/100
    return center, radius

# Program Loop
ret, frame = CAP.read()
origin, radius = find_origin(frame)
mx, my = 0,0
while True:
    ret, frame = CAP.read()
    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Identify Marker
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    marker_mask = cv2.inRange(hsv, MARKER_RANGE[0], MARKER_RANGE[1])
    marker_mask = cv2.dilate(marker_mask, KERNEL, iterations=1)
    
    contours,h = cv2.findContours(marker_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Checking if any contour is detected then run the following statements
    if len(contours) > 0:        
        # Get the biggest contour from all the detected contours
        cmax = max(contours, key = cv2.contourArea)
        # Find the area of the contour
        area = cv2.contourArea(cmax)
        # Checking if the area of the contour is greater than a threshold
        if area > MARKER_THRESHOLD:
            # Find center point of the contour
            M = cv2.moments(cmax)
            mx = int(M["m10"] / M["m00"])
            my = int(M["m01"] / M["m00"])
    else:
        previous_center_point= 0
    
    # Export Data

    # Output Image
    cv2.putText(frame,str('Marker: {},{}'.format(mx-origin[0], origin[1]-my)),(10,30), FONT, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.circle(frame, (int(origin[0]),int(origin[1])), 2, (0, 255, 0), 2)
    cv2.circle(frame, (int(origin[0]),int(origin[1])), int(radius), (255, 0, 0), 2)
    cv2.circle(frame, (int(mx),int(my)), 1, (0, 0, 255), 2)
    cv2.imshow('Detected Circles', frame)
    cv2.imshow('Mask', marker_mask)

# End While-Loop

CAP.release()
cv2.destroyAllWindows()