import numpy as np 
import cv2
from matplotlib import pyplot as plt 
img = cv2.imread('C:\\Users\\Lenovo\\Desktop\\aishwarya genietalk\\aishwarya negative images\\54.jpg',-1)
plt.imshow(img,cmap='gray',interpolation ='bicubic' )
plt.xticks([]),plt.yticks([])
plt.show()