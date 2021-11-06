import cv2, time 
# video obj with method for capturing video (0,1,2 = webcam or path to video)
# Trigger camera
video=cv2.VideoCapture(0)

# Frame obj for showing window which reads video obj
# check = bool / frame = 3D numpy array which rep img (first frame vid captures)
# Reads 1st Frame
check, frame = video.read()

print(check)
print(frame)

 # Loop through Frame array and use imshow to show each frame in the array

# this makes python wait for 3 seconds after turning on camera
time.sleep(3)
# Created window and showed 1st frame of video
cv2.imshow('Capturing',frame)
# Allows you to press any button and close window
cv2.waitKey(0)
# release camera
video.release()
# Closes window
cv2.destroyAllWindows