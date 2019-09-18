# Usage:
# python 023_canny.py --image images/006_coins.png

# Canny Edge Detector is a multi-step process involving blurring image to
# remove noise, computing Sobel gradient images in the x and y direction,
# suppressing edges, and a hysteresis thresholding stage to determine if a
# pixel is "edge-like" or not


# Import Needed Packages
import numpy as np
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Image")
args = vars(ap.parse_args())


# Load Image, Convert To Grayscale, Display
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.waitKey(0)

# Blur Image, Display
image = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Blurred", image)
cv2.waitKey(0)

# Perform Canny, Display
# cv2.canny(image, thresh_one, thresh_two)
canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)