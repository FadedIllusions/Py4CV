# AND, OR, NOT, XOR
# Binary In Manner; Therefore, Represented As Grayscale


# Import Needed Packages
import numpy as np
import cv2


# Define 300x300px Rectangle Of Zeros (Black)
rectangle = np.zeros((300,300), dtype="uint8")

# Using cv2.rectangle, Create Inner Rectangle
# From (25,25) to (275,275), White, Filled
cv2.rectangle(rectangle, (25,25), (275,275), 255, -1)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)

# Define Another Black, 300x300px Rectangle 
circle = np.zeros((300,300), dtype="uint8")

# Using cv2.circle, Create Inner Circle
cv2.circle(circle, (150,150), 150, 255, -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)


# AND Rectangle And Circle
bitwiseAND = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAND)
cv2.waitKey(0)

# OR Rectangle And Circle
bitwiseOR = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOR)
cv2.waitKey(0)

# XOR Rectangle And Circle
bitwiseXOR = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXOR)
cv2.waitKey(0)

# NOT Rectangle And Circle
bitwiseNOT = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNOT)
cv2.waitKey(0)