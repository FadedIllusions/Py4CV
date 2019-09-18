# Usage
# python 011_masking.py --image images/001_Image.jpg


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


# Create Mask, Find Image Center, Determine Masked Area, Show Mask
mask = np.zeros(image.shape[:2], dtype="uint8")
(cX,cY) = (image.shape[1]//2, image.shape[0]//2)
cv2.rectangle(mask, (cX+-50, cY-150), (cX+200, cY+75), 255, -1)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

# Mask And Display Image
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked Image", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()