# Usage
# python 012_splitting_and_merging.py --image images/001_Image.jpg


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

# Split BGR Image Into Seperate Channels
(B, G, R) = cv2.split(image)

# Show Channels
cv2.imshow("Red", R)
cv2.imshow("Blue", B)
cv2.imshow("Green", G)
cv2.waitKey(0)

# Merge Channels And Display Image
merged = cv2.merge([B,G,R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)

# Alternatively, To See Actual Color Of Channels.
#
# Create Empty NP Array
zeros = np.zeros(image.shape[:2], dtype="uint8")
# Merge And Display Each Channel With Np Array As Empty Channels
cv2.imshow("Red Scale", cv2.merge([zeros, zeros, R]))
cv2.imshow("Blue Scale", cv2.merge([B, zeros, zeros]))
cv2.imshow("Green Scale", cv2.merge([zeros, G, zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()