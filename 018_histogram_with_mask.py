# Usage
# python 018_histogram_with_mask.py --image images/005_beach.png


# Import Needed Packages
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2


def plot_histogram(image, title, mask=None):
	chans = cv2.split(image)
	colors = ("b", "g", "r")
	plt.figure()
	plt.title(title)
	plt.xlabel("Bins")
	plt.ylabel("# Of Pixels")
	
	for (chan, color) in zip(chans, colors):
		hist = cv2.calcHist([chan], [0], mask, [256], [0,256])
		plt.plot(hist, color=color)
		plt.xlim([0,256])
		
		
# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Image")
args = vars(ap.parse_args())


# Load And Display Image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Plot Histogram
plot_histogram(image, "Histogram Of Original Image")

# Define And Display Mask
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (15,15), (130,100), 255, -1)
cv2.imshow("Mask", mask)

# Apply Mask And Display
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied", masked)

# Apply And Display Histogram To Masked Image
plot_histogram(image, "Histogram Of Masked Image", mask=mask)
plt.show()
