import cv2
import numpy as np
from matplotlib import pyplot as plt

imggambar = cv2.imread("./Nomor6.jpg", -1)

# ===========
imgCropped = imggambar[50:150, 150:350]
cv2.imshow('original size Image', imggambar)
cv2.imshow("citra hasil crop", imgCropped)
# cv2.imshow("citra hasil crop",imggambar)
cv2.waitKey(0)
cv2.destroyAllWindows
