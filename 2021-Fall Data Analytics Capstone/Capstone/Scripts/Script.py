import cv2
import numpy as np

CAP = cv2.VideoCapture(0)
KERNEL = np.ones((10,10), np.uint8)
FIDUCIAL_THRESHOLD = 3000
FONT = cv2.FONT_HERSHEY_SIMPLEX

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
                       
    center = (int(x/100),int(y/100))
    radius = int(radius/100)
    return center, radius

# Program Loop
ret, frame = CAP.read()
origin, radius = find_origin(frame)
while True:
    ret, frame = CAP.read()
    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Identify Fiducial

    # Identify Marker

    # Export Data

    # Output Image
    cv2.putText(frame,str('C'.format()),(10,30), FONT, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.circle(frame, (origin[0],origin[1]), 2, (0, 255, 0), 2)
    cv2.circle(frame, (origin[0],origin[1]), radius, (255, 0, 0), 2)
    cv2.imshow('Detected Circles', frame)

# End While-Loop

CAP.release()
cv2.destroyAllWindows()