import cv2
import numpy as np

#Create two sample images
img1 = np.zeros((300, 300), dtype=np.uint8)
img2 = np.zeros((300, 300), dtype=np.uint8)

#Draw white rectangles
cv2.rectangle(img1, (50, 50), (200, 200), 255, -1)
cv2.rectangle(img2,(100, 100), (250,250), 255, -1)

#Apply bitwise AND
result = cv2.bitwise_and(img1, img2)

#Display images
cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("And Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()


# pip install opencv-python numpy