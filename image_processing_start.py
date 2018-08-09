import numpy as numpy
import cv2
img = cv2.imread('C:\\Users\\Lenovo\\Desktop\\aishwarya genietalk\\aishwarya negative images\\55.jpg',-1)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('messigray.png',img)
	cv2.destroyAllWindows()