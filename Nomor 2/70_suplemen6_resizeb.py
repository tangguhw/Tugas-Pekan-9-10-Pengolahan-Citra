import cv2
import numpy as np
from matplotlib import pyplot as plt


imggambar = cv2.imread("./Nomor2.jpg", -1)


imgresize = cv2.resize(imggambar, (300, 200))
cv2.imshow('original size Image', imggambar)
cv2.imshow("citra hasil", imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows
