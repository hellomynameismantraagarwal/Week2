
import cv2
import numpy as np

# 1. Load the road image
image = cv2.imread("roadwithcar.png")
image = cv2.resize(image, (700,900))

if image is None:
    raise FileNotFoundError("Could not load road.jpg")

# Display the original image
cv2.imshow("Original Image", image)

# 2. Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define white lane-marking color range
lower_white = np.array([0, 0, 180])
upper_white = np.array([180, 60, 255])

# Define yellow lane-marking color range
lower_yellow = np.array([15, 70, 100])
upper_yellow = np.array([40, 255, 255])

# Create masks for white and yellow
white_mask = cv2.inRange(hsv, lower_white, upper_white)
yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Combine the two masks
color_mask = cv2.bitwise_or(white_mask, yellow_mask)

cv2.imshow("HSV Color Mask", color_mask)

# 3. Apply Gaussian blur
blurred = cv2.GaussianBlur(color_mask, (5, 5), 0)

cv2.imshow("Gaussian Blur", blurred)

# 4. Apply Canny edge detection
edges = cv2.Canny(blurred, 50, 150)

cv2.imshow("Canny Edges", edges)

# 5. Create the Region of Interest (ROI) mask
height, width = edges.shape

roi_mask = np.zeros_like(edges)

polygon = np.array([[
    (int(width * 0.10), height - 1),
    (int(width * 0.90), height - 1),
    (int(width * 0.55), int(height * 0.55)),
    (int(width * 0.45), int(height * 0.55))
]], dtype=np.int32)

# Fill the road-shaped polygon with white
cv2.fillPoly(roi_mask, polygon, 255)

# Keep edges only inside the ROI
roi_edges = cv2.bitwise_and(edges, roi_mask)

cv2.imshow("ROI Mask", roi_mask)
cv2.imshow("Final Lane Edges", roi_edges)

# Save the final result
cv2.imwrite("lane_edges.jpg", roi_edges)

print("Processing complete!")
print("Final result saved as lane_edges.jpg")

# Wait until a key is pressed
cv2.waitKey(0)

# Close all image windows
cv2.destroyAllWindows()
