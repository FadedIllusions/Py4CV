# Usage:
# python 004_translation.py --image images/001_Image.jpg

import numpy as np
import argparse
import imutils
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Image")
args = vars(ap.parse_args())


# Load Image
image = cv2.imread(args["image"])

# Display Image
cv2.imshow("Original", image)
cv2.waitKey(0)


# Define Translation Matrix
# [1,0,tx] Shifts Image L-R, Negative Being To Left, Positive To Right
# [0,1,tx] Shift Image U-D, Negative Being Up, Positive Down
M = np.float32([[1,0,25], [0,1,50]])

# Shift Image By Translation Matrix
# warpAffine(image_to_shift, translation_matrix, dim_x, dim_y)
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# Display Shifted Image -- Down And Right
cv2.imshow("Translated Image", shifted)
cv2.waitKey(0)

# Redefine Translation Matrix, Shift Image, And Display  -- Up And Left
M = np.float32([[1,0,-50], [0,1,-90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Translated Image", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()