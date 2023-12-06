import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

# Baca citra
image = cv2.imread('citraB.jpg')

# Konversi citra ke HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Tampilkan citra asli dan citra dalam ruang warna HSV
cv2.imshow('Original Image', image)
cv2.imshow('HSV Image', hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
