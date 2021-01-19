import cv2

photo=cv2.VideoCapture(0)

for i in range(10):
    return_value, image = photo.read()
    cv2.imwrite(str(i)+'.jpg', image)
del(photo)

