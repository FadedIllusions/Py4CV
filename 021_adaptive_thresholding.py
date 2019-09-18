# Usage
# python 021_adaptive_thresholding.py --image images/006_coins.png

# We Need To Manually Supply Threshold Value T In Simple Thresholding, Often
# Requiring A Lot Of Experimentation. Not Very Helpful If Image Exhibits A Large
# Range In Pixel Intensities.
#
# Using Adaptive Thresholding, Which Considers Small Neighborhoods Of Pixels And
# Finds, An Optimal Threshold Value, T, For Each... Allowing Us To Handle Cases In
# Which There May Be Dramatic Ranges Of Pixel Intensities And The Optimal Value Of
# T May Change For Different Parts Of The Image.


# Import Needed Packages
import numpy as np
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Image")
args = vars (ap.parse_args())


# Load Image, Convert, Blur, Display
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image", image)
cv2.waitKey(0)


# Threshold Image And Display
# adaptiveThreshold(image, max, method, set vals greater than T to 0, neighborhood size, c-value)
# neighborhood size must be odd
# c-value is int subtracted from mean, allowing us to fine-tune our thresholding
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Mean Threshold", thresh)
cv2.waitKey(0)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Guassian Threshold", thresh)
cv2.waitKey(0)