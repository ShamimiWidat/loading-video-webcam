import cv2
import numpy as np

#define video capture
#0 refers first webcam of computer
cap = cv2.VideoCapture (0)

#to save the video
#cannot mp4 format cause convert from image processing
#frame persec, size pf video(size of webcam)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("flipped_video.avi", fourcc, 25, (640, 480))

#image per sec
while True:
    ret, frame = cap.read()
    print(frame.shape)
    frame2 = cv2.flip(frame, 0)#vertical
    frame3 = cv2.flip(frame, 1)#horizontal/mirror
    
    cv2.imshow("flipping vertical", frame2)
    cv2.imshow("flipping horizontal", frame3)
    cv2.imshow("frame", frame)

    #save video
    out.write(frame2)

    #0 if one image because it freeze
    #1 millisec before loop for another frame, take picture of every 1 millisec
    key = cv2.waitKey(1)
    if key == 27: #'Esc' key
        break

out.release()
cap.release()
cv2.destroyAllWindows()

#tak jadi pakai camera, video biasa jadi
