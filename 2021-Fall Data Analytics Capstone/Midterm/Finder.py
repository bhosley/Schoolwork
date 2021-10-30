# Hough circle detection

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
kernel = np.ones((10,10), np.uint8)
marker_threshold = 3000

while (1):
    ret, frame = cap.read()

    # Lets try a mask
    mask = cv2.inRange(frame, 
        np.array([0, 0, 0]),  # BGR Black
        np.array([75, 75, 75]))  # BGR lighter Black
    mask = cv2.dilate(mask, np.ones((10,10), np.uint8), iterations=1)
    #mask = cv2.bitwise_not(mask)

    edges = cv2.Canny(frame,250,550)

    try:
        # currently frame, may need to be HSV
        circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20,
                            param1=50, param2=40, minRadius=0, maxRadius=0)

        circles = np.uint16(np.around(circles))
        print(len(circles))
        print(circles)
        for i in circles[0, :]:
            # Draw the outer circle (blue)
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)

            # Draw the center of the circle (red)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
    except:
        pass

    contours,h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
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
            cv2.circle(frame, (mX, mY), 2, (0, 255, 0), 2)
    else:
        previous_center_point= 0

    #cv2.imshow('edges', edges)
    cv2.imshow('Mask', mask)    
    cv2.imshow('Detected Circles', frame)

    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()