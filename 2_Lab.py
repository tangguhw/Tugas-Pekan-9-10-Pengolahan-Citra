import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

# Baca citra
image = cv2.imread('citraB.jpg')

# Konversi citra ke ruang warna L*a*b*
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Tampilkan citra asli dan citra dalam ruang warna L*a*b*
cv2.imshow('Original Image', image)
cv2.imshow('L*a*b* Image', lab_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
