# Usage
# python 015_color_histograms.py --image images/001_Image.jpg

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
from __future__ import print_function
from matplotlib import pyplot as plt
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


# Split Channels
chans = cv2.split(image)

# Define Colors And Plot Parameters
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# Of Pixels")

# Iterate Over Channels
for (chan, color) in zip(chans, colors):
	# Create For Current Histogram And Plot
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	plt.plot(hist, color=color)
	plt.xlim([0, 256])
	plt.show()
	cv2.waitKey(0)
	

# Let's Automate Building 2D Histograms
fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0,1], None, [32,32], [0,256,0,256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram For G And B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0,1], None, [32,32], [0,256,0,256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram For G And R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0,1], None, [32,32], [0,256,0,256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram For B And R")
plt.colorbar(p)

plt.show()

print("2D Histogram Shape: {}, With {} Values".format(hist.shape, hist.flatten().shape[0]))
cv2.waitKey(0)