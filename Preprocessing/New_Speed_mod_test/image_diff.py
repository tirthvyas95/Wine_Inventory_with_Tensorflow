import cv2 as cv
import numpy as np

count =0

image1 = cv.imread("First.jpg")
image2 = cv.imread("Second.jpg")

diff = cv.subtract(image1, image2)

cv.imwrite("first2.jpg", diff)

imgray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#print(contours)
for contour in contours:
    area = cv.contourArea(contour)
    if area > 500:
        count = count + 1
        cv.drawContours(diff, contours, -1, (0, 255, 0), 3)

cv.imwrite("first3.jpg", diff)