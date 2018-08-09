import numpy as np 
import cv2
'''
cap = cv2.VideoCapture(0)
while(True):
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',gray)
	if cv2.waitKey(1)& 0xFF == ord('q'):
		break
cap.release() 
cv2.destroyAllWindows()
'''
cap = cv2.VideoCapture('C:\\Users\\Lenovo\\Desktop\\series\\friends\\s01\\Friends S01E01 720p HDTV x264 - The One Where Monica Gets a Roommate.mkv')
while(cap.isOpened()):
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()