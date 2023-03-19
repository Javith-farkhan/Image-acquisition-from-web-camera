#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import cv2
import numpy as np
VidCap=cv2.VideoCapture(0)
while(True):
    ret,frame=VidCap.read()
    cv2.imshow('image',frame)
    if cv2.waitKey(1) == ord('q'):
        break
VidCap.release()
cv2.destroyAllWindows()


# In[ ]:


import cv2
import numpy as np
VidCap=cv2.VideoCapture(0)
while(True):
    ret,frame=VidCap.read()
    cv2.imshow('video_image',frame)
    if cv2.waitKey(1) == ord('q'):
        break
VidCap.release()
cv2.destroyAllWindows()


# In[ ]:


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
    
    cv2.imshow('frame',image)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


# In[ ]:


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
    cv2.imshow('frame',image)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
