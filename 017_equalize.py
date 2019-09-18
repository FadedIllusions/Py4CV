# Usage:
# python 017_equalize.py --image images/005_beach.png

# Histogram Equalization
# Improves Contrast Of Image By 'Stretching' Distribution Of Pixels', Improving Global Contrast Of Image.
# (Applied To GrayScale Images). Useful When Image Contains Foregrounds And Backgrounds That Are Both Dark
# Or Both Light. Useful Enhancing Contrast Of Medical Or Satellite Imagery.


# Import Needed Packages
import numpy as np
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Image")
args = vars(ap.parse_args())


# Load, Convert, And Display Image
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Grayscale", image)
cv2.waitKey(0)

# Equalize Image Histogram
eq = cv2.equalizeHist(image)

# Display Equalized Image
cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)
cv2.destroyAllWindows()