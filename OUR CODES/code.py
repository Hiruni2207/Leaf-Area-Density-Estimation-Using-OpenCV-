import cv2
import numpy as np

# Read the image
IMG_PATH =r"Nursery\r1.png"
image = cv2.imread(IMG_PATH)
cv2.imshow("read", image)

# Convert to grayscale and apply Gaussian blur to reduce noise
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Use Canny edge detection to detect leaf edges
edges = cv2.Canny(blurred, 50, 150)

# Find contours (leaf shapes) from edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
# Create a mask for the leaves
leaf_mask = np.zeros_like(gray)

# Draw and fill the contours to capture the inside of the leaves
cv2.drawContours(leaf_mask, contours, -1, 255, thickness=cv2.FILLED)

# Treat water drops as part of the leaf area by not removing them
# Do not exclude water drops; they are naturally considered part of the leaves.

# Enhance intensity inside the leaf areas
image[leaf_mask == 255] = cv2.add(image[leaf_mask == 255], (30, 30, 30))  # Increase intensity

# Apply RGB thresholding for green color detection
lower_green = np.array([0, 132, 0], dtype=np.uint8)
upper_green = np.array([160, 255, 145], dtype=np.uint8)


# Mask for green color in the image
green_mask = cv2.inRange(image, lower_green, upper_green)

# Apply morphological closing to fill gaps in the green mask
kernel = np.ones((5, 5), np.uint8)
green_mask_closed = cv2.morphologyEx(green_mask, cv2.MORPH_CLOSE, kernel)

# Apply the final green mask to the original image
green_area = cv2.bitwise_and(image, image, mask=green_mask_closed)

# Calculate the leaf area density (percentage of green area)
green_pixels = cv2.countNonZero(green_mask_closed)
total_pixels = image.shape[0] * image.shape[1]
leaf_area_density = (green_pixels / total_pixels) * 100

print(f'Leaf Area Density: {leaf_area_density:.2f}%')

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Leaf Mask', leaf_mask)
cv2.imshow('Green Area', green_area)
cv2.waitKey(0)
cv2.destroyAllWindows()
