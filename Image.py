# -*- coding: utf-8 -*-
#Author:Little Tang
import numpy as np
import cv2
image = cv2.imread("C:/Users/Administrator/Desktop/test.jpg")
cv2.imshow("Original",image)
cv2.waitKey(0)
#彩色转灰色
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
cv2.waitKey(0)