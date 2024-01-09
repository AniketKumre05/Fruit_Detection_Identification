import cv2

cap=cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    cv2.imshow('img',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
