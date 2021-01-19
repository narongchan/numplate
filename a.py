import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
config = r'-l kor --psm 7 --oem 1 --tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

img_ori = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)

chars = pytesseract.image_to_string(img_ori,config=config)
    

print(chars)