# Usage
# python 013_colorspaces.py --image images/001_Image.jpg


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
cv2.waitKey(0)

# Convert To Grayscale And Display
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

# Convert To HSV And Display
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# Convert To LAB And Display
lab = cv2.cvtColor(image, cv2.COLORBGR2LAB)
cv2.imshow("LAB", lab)
cv2.waitKey(0)
cv2.destroyAllWindows()