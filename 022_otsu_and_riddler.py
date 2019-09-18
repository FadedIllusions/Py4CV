# Usage
# python 022_otsu_and_riddler.py --image images/006_coins.png

# Otsu's method assumes two peaks in grayscale histogram, then tries
# to find an optimal value to seperate these peaks.


# Import Needed Packages
from __future__ import print_function
import numpy as np
import argparse
import mahotas
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Image")
args = vars(ap.parse_args())


# Load Image, Convert, Blur, Display
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image", image)

# Obtain Otsu T Value
T = mahotas.thresholding.otsu(blurred)
print("Otsu's Threshold: {}".format(T))

# Create Threshold Image Based On Otsu's T Value, Display
thresh = image.copy()
thresh[thresh>T] = 255
thresh[thresh<T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)
cv2.waitKey(0)

# Obtain Riddler-Calvard T Value, Threshold Image, Display
T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh>T] = 255
thresh[thresh<T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)