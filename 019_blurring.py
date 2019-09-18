# Usage
# python 019_blurring.py --image images/005_beach.png


# Import Needed Packages
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


# Average Blurring
#
# Define k x k Convolutional Kernel Wherein The Center Pixel
# Of Matrix Is Average Of All Surrounding Pixels
blurred = np.hstack([
						cv2.blur(image, (3,3)),
						cv2.blur(image, (5,5)),
						cv2.blur(image, (7,7))])

# Display Horizontal Stack Of Averaged Images
# Note That The Larger The Convolutional Matrix,
# The More Blurred The Image
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)


# Gaussian Blurring
#
# Rather Than Using Simple Mean Of Average Blurring, Uses Weighted Mean
# Wherein Neighboring Pixels Closer To Center Pixel Contribute More "Weight"
# Last Parameter Is Sigma -- Standard Deviation In X-Axis Direction
# Setting It To 0 Instructs OCV To Automatically Compute Based On Kernel Size
blurred = np.hstack([
						cv2.GaussianBlur(image, (3,3), 0),
						cv2.GaussianBlur(image, (5,5), 0),
						cv2.GaussianBlur(image, (7,7), 0)])

cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)


# Median Blurring
#
#  Unlike Averaging, Instead Of Replacing Central Pixel With Average,
# We Replace Central Pixel With Mean Of Neighborhood
blurred = np.hstack([
						cv2.medianBlur(image, 3),
						cv2.medianBlur(image, 5),
						cv2.medianBlur(image, 7)])

cv2.imshow("Median", blurred)
cv2.waitKey(0)


# Bilateral Blurring
#
# Reduces Noise Whilst Maintaining Edge By Introducing Two Gaussian Distributions
# First Distribution Only Considers Spatial Neighbors
# Second Models Pixel Intensity Of Neighborhood, Ensuring Only Pixels With Similar
# Intensity Are Included In Computation Of Blur
#
# cv2.bilaterFilter(image-to-blur, diameter-of-neighborhood, color-sigma, spatial-sigma)
# Large Color Sigma Means More Colors Considered
# Larger Spatial Sigma, Pixels Further From Central Will Influence Calculation,
# Providing Their Colors Are Similar Enough
blurred = np.hstack([
						cv2.bilateralFilter(image, 5, 21, 21),
						cv2.bilateralFilter(image, 7, 31, 31),
						cv2.bilateralFilter(image, 9, 41, 41)])

cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)