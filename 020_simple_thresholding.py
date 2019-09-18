# Usage
# python 020_simple_thresholding.py --image images/006_coins.png

# Thresholding Is The Binarization Of An Image. We Seek A GrayScale Image
# To A Binary Image Wherein Pixels Are Either 0 Or 255.
#
# In Simple Example, Select A Pixel Value p. All Pixel Intensities Less Than
# p Are Set To 0, All Values Greater Set To 255.


# Import Needed Packages
import numpy as np
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Image")
args = vars(ap.parse_args())


# Load Image, Convert To GrayScale, Blur, Display
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image", image)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)


#
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverted", threshInv)
cv2.waitKey(0)

cv2.imshow("Coins", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)
cv2.destroyAllWindows()