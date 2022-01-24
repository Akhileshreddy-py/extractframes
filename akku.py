import cv2
cap=cv2.VideoCapture("v.mp4")
count=0
while True:
    t,f=cap.read()
    f=cv2.resize(f,(600,400))
    cv2.imshow("akhi",f)
    cv2.imwrite("images/a"+str(count)+".jpg",f)
    count=count+1
    cv2.waitKey(30)