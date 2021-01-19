import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot  as plt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
config = r'-l kor --psm 7 --oem 1 --tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'
plt.style.use("dark_background")

cv2.VideoCapture(0)



while photo < 10:
    img_ori = cv2.imread(str(photo)+'.jpg', cv2.IMREAD_GRAYSCALE)

    height, width= img_ori.shape

    chars = pytesseract.image_to_string(img_ori,config=config)


    print(chars)
    plt.figure(figsize=(12,10))
    plt.imshow(img_ori)
    plt.show()
    photo = photo+1