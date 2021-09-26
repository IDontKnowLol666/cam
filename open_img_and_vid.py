import cv2

cam = cv2.VideoCapture(0)

from properties import sent
Password = 'B00fu123'
cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 32:
        img_name = "opencv_frame_0.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        print(img_name)
    elif k%256 == 27:
        sent()

cam.release()

cv2.destroyAllWindows()
