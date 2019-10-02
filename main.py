import cv2
import numpy as np
import glob
import os

images = glob.glob("./processed/*_middle.jpg")
counter = 0
for image in images:
    print(image)
    im = cv2.imread(image)
    # print(im.shape)

    # left = im[:, :int(im.shape[1]/3)]
    # middle = im[:, int(im.shape[1]/3):int(im.shape[1]/3*2)]
    # right = im[:, int(im.shape[1]/3*2):]

    # left = im[:, :int(im.shape[1]/3)]
    # middle = im[:, int(im.shape[1]/3):int(im.shape[1]/3*2)]
    # right = im[:, int(im.shape[1]/3*2):]

    top = im[:649]
    middle = im[649:1296]

    cv2.imwrite("./processed/{}_middle.jpg".format(counter), middle)
    # cv2.imwrite("./processed/{}_middle.jpg".format(counter), middle)
    # cv2.imwrite("./processed/{}_right.jpg".format(counter), right)
    counter += 1