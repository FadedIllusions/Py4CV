# Usage
# python 014_grayscale_histogram.py --image images/001_Image.jpg

# Histograms Represent Distribution Of Pixel Intensities (Color Or Grayscale)
# X-Axis: Bins
# Y-Axis: Num Of Pxs Binned To X-Axis
# If Using 256 Bins With RGB Image, We Are Effectively Counting Number Of
# Times Each Pixel Value Occurs. In Contrast, If We Use Only 2 (Equally Spaced)
# Bins, We Are Counting Number Of Times A Px Is In Range [0,128) or [128,255].

# cv2.calcHist(image, channels, mask, histSize, ranges)
# Ex: cv2.calcHist(image, [0,1,2], None, [32,32,32], [0,256])
# Calculate Histogram for 'image', all RGB channels, No Mask, 32 Bins Per Channel, For Full Range


# Import Needed Packages
from matplotlib import pyplot as plt
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

# Convert To Grayscale And Display
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)

# Calculate And Define Histogram
# Grayscale Hist On 'image', Only Channel, No Mask, 256 Bins, Range 0-256
hist = cv2.calcHist([image], [0], None, [256], [0,256])

# Plot Histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# Of Pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()