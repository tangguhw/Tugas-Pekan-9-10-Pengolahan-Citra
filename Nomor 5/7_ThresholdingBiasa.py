import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

# Baca citra dalam mode grayscale
image = cv2.imread('./Nomor5.jpg', 0)  # Mode 0 untuk citra grayscale

# Tentukan nilai threshold secara manual (misalnya, 127)
threshold_value = 127

# Menggunakan thresholding biasa
_, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# Tampilkan citra asli dan citra hasil thresholding
cv2.imshow('Original Image', image)
cv2.imshow('Thresholding Biasa', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
