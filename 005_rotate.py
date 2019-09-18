# Usage:
# python 005_rotate.py --image images/001_Image.jpg

import numpy as np
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Image")
args = vars(ap.parse_args())


# Load And Display Original Image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# Obtain Dimensions And Center-Point Of Image
(h,w) = image.shape[:2]
center = (w//2, h//2)


# Create Rotational Matrix
# From Center-Point, Rotate 45 Degrees CCW With Scale Of 100%
M = cv2.getRotationMatrix2D(center, 45, 1.0)

# Rotate Image And Display
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)


# Create Rotational Matrix (90d CW), Rotate, Display Image
M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()