# Usage
# python 006_resize.py --image images/001_Image.jpg


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


# Define Apect Ratio Of Desired Width To Current Width
# Resize To 150px, Using Aspect Ratio
r = 150.0/image.shape[1]
dim = (150, int(image.shape[0]*r))

# Resize Image (Width) And Display
# Have : INTER_AREA, INTER_LINEAR, INTER_CUBIC
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)


# Define New Aspect Ratio
r = 50.0/image.shape[0]
dim = (int(image.shape[1]*r), 50)

# Resize Image (Height) And Display
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()