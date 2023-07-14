"""filter.py"""
import sys

import cv2
import numpy as np

IMAGE_FULLPATH = sys.argv[1]
IMAGE_NAME = sys.argv[2]
FILTER = sys.argv[3]
if FILTER == "Sketch Style":  # sketch
    img = cv2.imread(str(IMAGE_FULLPATH))
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    invertedblur = cv2.bitwise_not(blur)
    image = cv2.divide(grey_img, invertedblur, scale=256.0)
    cv2.imwrite("media/image.jpg", image)
    print("image.jpg", end="")
elif FILTER == "Increase Brightness":  # increase brightness
    img = cv2.imread(str(IMAGE_FULLPATH))
    Intensity_Matrix = np.ones(img.shape, dtype="uint8") * 60
    image = cv2.add(img, Intensity_Matrix)
    cv2.imwrite("media/image.jpg", image)
    print("image.jpg", end="")
elif FILTER == "Decrease Brightness":  # decrease brightness
    img = cv2.imread(str(IMAGE_FULLPATH))
    Intensity_Matrix = np.ones(img.shape, dtype="uint8") * 60
    dark = cv2.subtract(img, Intensity_Matrix)
    cv2.imwrite("media/image.jpg", dark)
    print("image.jpg", end="")
elif FILTER == "Blur":  # blur
    img = cv2.imread(str(IMAGE_FULLPATH))
    image = cv2.blur(img, (50, 50))
    cv2.imwrite("media/image.jpg", image)
    print("image.jpg", end="")
elif FILTER == "Black & White":  # grayscale
    img = cv2.imread(str(IMAGE_FULLPATH))
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("media/image.jpg", image)
    print("image.jpg", end="")
elif FILTER == "Size Downscale":  # downsize
    img = cv2.imread(str(IMAGE_FULLPATH))
    DOWN_WIDTH = 300
    DOWN_HEIGHT = 200
    down_points = (DOWN_WIDTH, DOWN_HEIGHT)
    image = cv2.resize(img, down_points, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite("media/image.jpg", image)
    print("image.jpg", end="")
elif FILTER == "Size Upscale":  # upsize
    img = cv2.imread(str(IMAGE_FULLPATH))
    UP_WIDTH = 600
    UP_HEIGHT = 400
    up_points = (UP_WIDTH, UP_HEIGHT)
    image = cv2.resize(img, up_points, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite("media/image.jpg", image)
    print("image.jpg", end="")
elif FILTER == "Horizontal Flip":  # horizontal flip
    img = cv2.imread(str(IMAGE_FULLPATH))
    image = cv2.flip(img, 1)
    cv2.imwrite("media/image.jpg", image)
    print("image.jpg", end="")
elif FILTER == "Vertical Flip":  # vertical flip
    img = cv2.imread(str(IMAGE_FULLPATH))
    image = cv2.flip(img, 0)
    cv2.imwrite("media/image.jpg", image)
    print("image.jpg", end="")
elif FILTER == "Rotate":  # rotate
    img = cv2.imread(str(IMAGE_FULLPATH))
    image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite("media/image.jpg", image)
    print("image.jpg", end="")
elif FILTER == "Inverted Colour":  # invert
    img = cv2.imread(str(IMAGE_FULLPATH))
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    cv2.imwrite("media/image.jpg", invert)
    print("image.jpg", end="")
