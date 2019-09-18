# Import Needed Packages
import numpy as np
import cv2

# Create 300x300px RGB Canvas, Filled With Zeros
canvas = np.zeros((300,300,3), dtype="uint8")

# Draw Green Line On Canvas
# From Top-Left To Bottom-Right
green = (0,255,0)
cv2.line(canvas, (0,0), (300,300), green)

# Display Canvas
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw Red Line On Canvas
# Frin Bottom-Left To Top-Right With Thickness Of 3
red = (0,0,255)
cv2.line(canvas, (300,0), (0,300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw Green Rectangle On Canvas
cv2.rectangle(canvas, (50,50), (250,250), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw Red Circle On Canvas
# Starting At Center Of Canvas, With Radius 50, And Thickness 3
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
cv2.circle(canvas, (centerX,centerY), (50), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# Create Fresh Canvas
canvas = np.zeros((300,300,3), dtype="uint8")

# Starting From Center Of Canvas, Draw Bullseye Pattern
for r in range(0,150,25):
	cv2.circle(canvas, (centerX, centerY), r, (255,255,255), 2)

# Display Bullseye Canvas
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# Create Canvas For Abstract Drawing
canvas = np.zeros((300,300,3), dtype="uint8")

for i in range(0,25):
	radius = np.random.randint(5, high=200)
	color = np.random.randint(0, high=256, size=(3,)).tolist()
	pt = np.random.randint(0, high=300, size=(2,))
	cv2.circle(canvas, tuple(pt), radius, color, -1)
	
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)