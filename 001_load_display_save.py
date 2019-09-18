# Usage
# python 001_load_display_save.py --image images/001_Image.jpg

# Import Needed Packages
from __future__ import print_function
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Image")
args = vars(ap.parse_args())


# Load Image, Print Dims To Console
image = cv2.imread(args["image"])
print("Width: {} Pixels".format(image.shape[1]))
print("Height: {} Pixels".format(image.shape[0]))
print("Channels: {}".format(image.shape[2]))
# When Represented By NumPy Array: 
# (Height, Width, Channels) ... (Rows, Columns, Depth)
# With [0,0] Representng Upper Left Corner

# Display Image Until Keypress
cv2.imshow("Loaded Image", image)
cv2.waitKey(0)


# Save Image To Disk
cv2.imwrite("images/002_NewSavedImage.jpg", image)