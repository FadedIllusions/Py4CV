# Usage:
# python 007_flipping.py --image images/001_Image.jpg


# Import Needed Packages
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


# Flip Image And Display
flipped = cv2.flip(image, 1)
cv2.imshow("Horizontal Flip", flipped)
cv2.waitKey(0)

# Flip Image And Display
flipped = cv2.flip(image, 0)
cv2.imshow("Vertical Flip", flipped)
cv2.waitKey(0)

# Flip Image And Display
flipped = cv2.flip(image, -1)
cv2.imshow("Horizontal And Vertical Flip", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()