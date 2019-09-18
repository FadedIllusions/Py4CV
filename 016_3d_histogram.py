# Usage
# python 016_3d_histogram.py --image images/001_Image.jpg


# Import Needed Packages
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Image")
ap.add_argument("-s", "--size", required=False, help="Size Of Largest Color Bin", default=5000)
ap.add_argument("-b", "--bins", required=False, help="Num Of Bins Per Channel", default=8)
args = vars(ap.parse_args())


# Load Parsed Arguments
image = cv2.imread(args["image"])
size = float(args["size"])
bins = int(args["bins"])

# Display Image
cv2.imshow("Original", image)
cv2.waitKey(0)

# Calculate Histogram
hist = cv2.calcHist([image], [0, 1, 2], None, [bins, bins, bins], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: %s, with %d values" % (hist.shape, hist.flatten().shape[0]))

# Define Plot And Iterate Through
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ratio = size / np.max(hist)

for (x, plane) in enumerate(hist):
	for (y, row) in enumerate(plane):
		for (z, col) in enumerate(row):
			if hist[x][y][z] > 0.0:
				siz = ratio * hist[x][y][z]
				rgb = (z/(bins-1), y/(bins-1), x/(bins-1))
				ax.scatter(x, y, z, s = siz, facecolors = rgb)
plt.savefig("images/004_3D_Histogram.png")
plt.show()