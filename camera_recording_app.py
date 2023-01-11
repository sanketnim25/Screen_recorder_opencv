import numpy as np
import cv2
a = cv2.VideoCapture(0)  # Create an object to read from camera

width = int(a.get(3))    # We need to set resolutions.
height = int(a.get(4))   # so, convert them from float to integer.
size = (width, height)
result = cv2.VideoWriter('filename.avi',                    # Below VideoWriter object will create 
                         cv2.VideoWriter_fourcc(*'MJPG'),   # a frame of above defined The output
                         30, size)                          # is stored in 'filename.avi' file.

while True:
    ret , frame = a.read()
    result.write(frame)                                      # Write the frame into the, file 'filename.avi'
    image = np.zeros(frame.shape , np.uint8)
    smaller_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    image[:height//2,:width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:,:width//2] = smaller_frame
    image[:height//2,width//2:] = smaller_frame
    image[height//2:,width//2:] = smaller_frame
    
    cv2.imshow("my_webcam",image)                          #cv2.imshow('Frame', frame) will show frame

    if cv2.waitKey(1) == ord("q"):                         # press q to quit
        break

# When everything done, release 
# the video capture and video 
# write objects
a.release()
result.release()
# Closes all the frames
cv2.destroyAllWindows()