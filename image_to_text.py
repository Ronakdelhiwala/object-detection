# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 22:06:48 2018

@author: RD
"""

import cv2
from PIL import Image
from pytesseract import image_to_string
import pytesseract
img = cv2.imread('gugal.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('agarbatti.png',gray)
img1 = Image.open('agarbatti.png')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
print (image_to_string(img1))


