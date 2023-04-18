#python BlackBorders.py -i 1.jpg -p E:\LAPTOP\STUDIA\II st PW LiK\MAGISTERKA\Omar Salloum\zdjecia\1.jpg
#python BlackBorders.py image E:\LAPTOP\STUDIA\II st PW LiK\MAGISTERKA\Omar Salloum\zdjecia\1.jpg
import argparse
import cv2
import imutils
import numpy as np
import os
from pathlib import Path
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument( "-i","--image",required=True,
                 help="path to input image")
ap.add_argument("-o", "--output", required=True,
	            help="path to output image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])


# print(image.shape)
width = image.shape[1]
height = image.shape[0]

# x = 60
# y = 20
# w = width - 170
# h = height - 80


x = int(0.12 * width)
y = int(0.0299 * height)
w = int(0.66 * width) 
h = int(0.88 * height)


mask = np.zeros(image.shape[:2],np.uint8)
mask[y:y+h,x:x+w] = 255
res = cv2.bitwise_and(image,image,mask = mask)

#defining a kernel
k_sharped = np.array([[0,-1,0],
                        [-1,5,-1],
                        [0,-1,0]])

sharpened = cv2.filter2D(res, -1, k_sharped)



cv2.imwrite(f'{args["output"]}', sharpened)

# cv2.imshow('Borders', sharpened)
# cv2.waitKey(0)
# cv2.destroyAllWindows()