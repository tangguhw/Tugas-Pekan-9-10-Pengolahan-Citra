import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

# Baca citra
image = cv2.imread('citraB.jpg')

# Konversi citra ke grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Tampilkan citra asli dan citra dalam skala keabuan
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
