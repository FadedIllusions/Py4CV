# Usage:
# python 009_arithmetic.py --image images/001_Image.jpg

# RGB Images Pixel Range: [0,255]
# What Happens If We Have 250 And Try To Add 10?
# CV Arithmetic: Clips At 255
# Numpy Arithmetic: Wraps Around To 4


# Import Needed Packages
from __future__ import print_function
import numpy as np
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Image")
args = vars(ap.parse_args())


# Load And Display Image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)


# Statement Prints
#
# Constrained
print("Max Of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("Min Of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
#
# Wrapped
print("Wrap Around: {}".format(np.uint8([200]) + np.uint8([100])))
# 200 + 100 = 300 ... 300 - 255 = 45 ... Zero Indexed: 44
print("Wrap Around: {}".format(np.uint8([50]) - np.uint8([100])))
# 50 - 100 = -50 ... Zero Index: 49 ... 255 - 49 = 206


# Construct Transformation (Addition) Matrix
# Add To And Display Image
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)
cv2.waitKey(0)

# Construct Transformation (Subtraction) Matrix
# Subtract From And Display Image
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)