import cv2
import numpy as np

k = cv2.imread("roadwithcar.png")
k = cv2.resize(k, (600,800))
h = cv2.cvtColor(k, cv2.COLOR_BGR2HSV)
ka = cv2.imread("HSV.png")
kah = cv2.cvtColor(ka, cv2.COLOR_BGR2HSV)
lower_white = np.array([0, 0, 180])
upper_white = np.array([180, 60, 255])
lower_yellow = np.array([15, 70, 100])
upper_yellow = np.array([40, 255, 255])
ly1 = np.array([1, 7, 10])
ly2 = np.array([40, 255, 255])
masy = cv2.inRange(k, lower_yellow, upper_yellow)
masw = cv2.inRange(k, lower_white, upper_white)
colormask = cv2.bitwise_or(masy, masw)

cv2.imshow("AA", colormask)




cv2.waitKey(0)
cv2.destroyAllWindows()