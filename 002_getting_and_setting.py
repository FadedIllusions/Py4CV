# Usage
# python 002_getting_and_setting.py --image images/001_Image.jpg


# Import Needed Packages
from __future__ import print_function
import argparse
import cv2


# Construct Argument Parser And Parse Argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Image")
args = vars(ap.parse_args())


# Load And Display Image
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)


# Split Color Channels
(b,g,r) = image[0,0]
print("Pixel At (0,0) -- Red: {}, Green: {}, Blue: {}".format(r,g,b))

# Reassign Pixel (0,0) Color
image [0,0] = (255,255,255)
(b,g,r) = image[0,0]
print("Pixel At (0,0) -- Red: {}, Green: {}, Blue: {}".format(r,g,b))

# Cut Image To Include Only Top-Left Corner, 100x100px
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

# Convert Entire Corner To Green
image[0:100, 0:100] = (0,255,0)

# Display Updated Image
cv2.imshow("Updated", image)
cv2.waitKey()