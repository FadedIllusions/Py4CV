# Usage
# python 024_counting_coins.py --image images/006_coins.png

# A contour is a curve of points, without any gaps in the curve.
# Well, first, need to obtain a binarization of the image, using
# edge detection or thresholding.


# Import Needed Packages
from __future__ import print_function
import numpy as np
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Image")
args = vars(ap.parse_args())


# Load Image, Cvt To GS, Blue, Display
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11,11), 0)
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

# Find Edges, Display
edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)
cv2.waitKey(0)

# Find Contours Of Edged Image
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("I count {} coins in this image".format(len(cnts)))

# Draw Contours Onto Image
coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0,255,0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)
cv2.destroyAllWindows()

for (i,c) in enumerate (cnts):
	(x,y,w,h) = cv2.boundingRect(c)
	
	print("Coin #{}".format(i+1))
	coin = image[y:y+h, x:x+w]
	cv2.imshow("Coin", coin)
	
	mask = np.zeros(image.shape[:2], dtype="uint8")
	((centerX,centerY), radius) = cv2.minEnclosingCircle(c)
	cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
	mask = mask[y:y+h, x:x+w]
	
	cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask=mask))
	cv2.waitKey(0)