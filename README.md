# Image-Acquisition-from-Web-Camera
## Aim
 
Aim:
 
To write a python program using OpenCV to capture the image from the web camera and do the following image manipulations.
i) Write the frame as JPG 
ii) Display the video 
iii) Display the video by resizing the window
iv) Rotate and display the video

## Software Used
Anaconda - Python 3.7
## Algorithm
### Step 1:
<br>
Use VideoCapture(0) to access web camera

### Step 2:
<br>
Use imread to read the video or image

### Step 3:
<br>
Use imwrite to save the image

### Step 4:
<br>
Use imshow to show the video

### Step 5:
<br>
End the program and close the output video windows by pressing 'q'.

## Program:

### Developed By: Javith Farkhan
### Register No: 212221240017

## i) Write the frame as JPG file
```
import cv2
videocaptureobject=cv2.VideoCapture(0)
while True:
    ret,frame=videocaptureobject.read()
    cv2.imwrite("videoimage.jpg",frame)
    if cv2.waitKey(1) == ord('q'):
        break
videocaptureobject.release()
cv2.destroyAllWindows()
```

## ii) Display the video

```
import cv2
videocaptureobject=cv2.VideoCapture(0)
while True:
    ret,frame=videocaptureobject.read()
    cv2.imshow("videoimage.jpg",frame)
    if cv2.waitKey(1) == ord('q'):
        break
videocaptureobject.release()
cv2.destroyAllWindows()

```

## iii) Display the video by resizing the window
```
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    
    image=np.zeros(frame.shape,np.uint8)
    smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    image[:height//2,:width//2]=smaller_frame
    image[height//2:,:width//2]=smaller_frame
    image[:height//2,width//2:]=smaller_frame
    image[height//2:,width//2:]=smaller_frame
    
    cv2.imshow('new',image)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

```


## iv) Rotate and display the video
```
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    
    image=np.zeros(frame.shape,np.uint8)
    smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    image[:height//2,:width//2]=smaller_frame
    image[height//2:,:width//2]=cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[:height//2,width//2:]=smaller_frame
    image[height//2:,width//2:]=cv2.rotate(smaller_frame,cv2.ROTATE_180)
    cv2.imshow('new',image)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

```
## Output

### i) Write the frame as JPG image

![first](https://user-images.githubusercontent.com/94296805/226169682-6df370e7-ee9a-4c63-91af-77237841e0e6.png)


### ii) Display the video
![second](https://user-images.githubusercontent.com/94296805/226169687-af677d47-8162-4b48-9593-fceaf0502afe.png)


### iii) Display the video by resizing the window
![quadrant](https://user-images.githubusercontent.com/94296805/226169692-338855c2-a14a-44c4-b970-3e669b5d5763.png)


### iv) Rotate and display the video

![rotate](https://user-images.githubusercontent.com/94296805/226169700-9d4fadf0-4317-4f06-b1d7-bf876686d020.png)





## Result:
Thus the image is accessed from webcamera and displayed using openCV.
