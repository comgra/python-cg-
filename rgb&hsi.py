import cv2
import numpy as np

img = np.zeros((200, 200, 3), dtype=np.uint8)
img[:] = (0, 0, 255)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imshow("BGR - Red", img)
cv2.imshow("HSV (visualized as BGR)", hsv_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()
