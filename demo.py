import cv2
## 窗口显示摄像头帧
clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_RBUTTONUP:
        clicked = True

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)

print('点击任意键停止')
success, frame = cameraCapture.read();
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('MyWindow', frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('MyWindow')
cameraCapture.release()

