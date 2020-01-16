import cv2
import os
# 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2

cap = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier('C:/Users/Administrator/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

face_id = input('\n enter user id:')

print('\n Initializing face capture. Look at the camera and wait ...')

count = 0

while True:

    # 从摄像头读取图片

    sucess, img = cap.read()

    # 转为灰度图片

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 检测人脸

    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    # 1、待检测图片 2、前后两次相继的扫描中搜索窗口的比例系数 3、构成检测目标的相邻矩形的最小个数
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+w), (255, 0, 0)) #1、原图 2、矩阵左上坐标 3、矩阵右下坐标 4、换线对应的rgb 5、画线的宽度
        count += 1

        # 保存图像
        cv2.imwrite("Facedata/User." + str(face_id) + '.' + str(count) + '.jpg', gray[y: y + h, x: x + w])

        cv2.imshow('image', img)

    # 保持画面的持续。

    k = cv2.waitKey(1)

    if k == 27:   # 通过esc键退出摄像
        break

    elif count >= 1:  # 得到1000个样本后退出摄像
        break

# 关闭摄像头
cap.release()
cv2.destroyAllWindows()