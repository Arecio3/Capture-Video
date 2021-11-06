import cv2
# video obj with method for capturing video 0,1,2 = camera or path to video
video=cv2.VideoCapture(0)
# release camera
video.release()