import numpy as np
import cv2
from pylab import *
img=cv2.imread("F:/rl/pichost/5.jpg",1)# 读取图片
color = (0, 255, 0)
face_patterns=cv2.CascadeClassifier('C:/Users/Administrator/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faceRects = face_patterns.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32)) # 人脸检测
if len(faceRects) > 0: # Large to 0,then it is a face
    for faceRect in faceRects:  
        x, y, w, h = faceRect
        cv2.rectangle(img, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 3) 
#writen to image

font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'Bset regards! From Argmin2018.',(1,40),font,1.2,(14,26,25),2)
cv2.imwrite('output.jpg',img) # 保存图片
cv2.imshow("Find Faces!",img)# 显示图片
cv2.waitKey(0)
