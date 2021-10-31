import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)

# Kernel to enhance the size of the marker_mask
kernel = np.ones((10,10), np.uint8)

# Laser color detection range, 
# red for testing purposes.
lower_marker = np.array([0, 0, 255])
upper_marker = np.array([255, 255, 255])
# Set threshold size for detecting marker blob
marker_threshold = 1000

while (1):

    # Take each frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    marker_mask = cv2.inRange(hsv, lower_marker, upper_marker)
    marker_mask = cv2.dilate(marker_mask, kernel, iterations=1)
    
    contours,h = cv2.findContours(marker_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Checking if any contour is detected then run the following statements
    if len(contours) > 0:        
        # Get the biggest contour from all the detected contours
        cmax = max(contours, key = cv2.contourArea)
        # Find the area of the contour
        area = cv2.contourArea(cmax)
        # Checking if the area of the contour is greater than a threshold
        if area > marker_threshold:
            # Find center point of the contour
            M = cv2.moments(cmax)
            mX = int(M["m10"] / M["m00"])
            mY = int(M["m01"] / M["m00"])
    else:
        previous_center_point= 0

    # Demonstrate Output; write coordinates to mask frame, circle in plain frame
    try:
        cv2.putText(marker_mask,str('{},{}'.format(mX,mY)),(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
        cv2.circle(frame, (mX, mY), 10, (0, 255, 0), 2)
    except:
        pass
    
    # Show each video stream
    cv2.imshow('marker_mask', marker_mask)
    cv2.imshow('Track Laser', frame)

    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()