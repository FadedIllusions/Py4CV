# Usage:
# python 008_cropping.py --image images/001_Image.jpg


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

print(image.shape[1])

# Crop And Display Image
# image[start_x:start_y, end_x:end_y]
# image[TH:BH, TW:BW]
cropped = image[220:450, 605:835]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)

	