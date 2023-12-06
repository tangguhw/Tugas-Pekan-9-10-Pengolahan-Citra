import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

# Baca citra dalam mode grayscale
image = cv2.imread('./Nomor6.jpg', 0)  # Mode 0 untuk citra grayscale

# Menggunakan Otsu's Thresholding
_, binary_image = cv2.threshold(
    image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Tampilkan citra asli dan citra hasil thresholding
cv2.imshow('Original Image', image)
cv2.imshow('Otsu Thresholding', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
