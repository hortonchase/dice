import cv2
import imutils
import time
vs = cv2.VideoCapture(0)
time.sleep(2)
while True:
    cap = vs.read()[1]
#    cv2.imshow("image", cap)
    gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
#    cv2.imshow("gray", gray)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
#    cv2.imshow("blur", gray)
    thresh = cv2.threshold(blur, 190, 255, cv2.THRESH_BINARY)[1]
    print(thresh.shape)
#    cv2.imshow("thresh", thresh)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:12]
    image = cap.copy()
    for c in cnts:
        cv2.drawContours(image, [c], 0, (0, 255, 0), 2)
#    cv2.imshow("cont", image)
    total = len(cnts)
    final = cv2.putText(cap.copy(), "Total: {}".format(total), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0, 2))
    cv2.imshow("final", final)
    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
