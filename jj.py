
import cv2
import numpy as np

# ==========================================
# 1. LOAD IMAGE
# ==========================================

image_path = "/home/mantra/Desktop/Workstuff/CEAM CV/Week2/acha.png"

image = cv2.imread(image_path)

if image is None:
    print("Error: Image could not be loaded.")
    raise SystemExit

image = cv2.resize(image, (1000, 700))
original = image.copy()

height, width = image.shape[:2]


# ==========================================
# 2. DETECT YELLOW AND WHITE PIXELS
# ==========================================

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Yellow markings
lower_yellow = np.array([15, 70, 100])
upper_yellow = np.array([40, 255, 255])

yellow_mask = cv2.inRange(
    hsv, lower_yellow, upper_yellow
)

# White markings
lower_white = np.array([0, 0, 170])
upper_white = np.array([179, 60, 255])

white_mask = cv2.inRange(
    hsv, lower_white, upper_white
)

# Combine yellow and white
lane_mask = cv2.bitwise_or(
    yellow_mask, white_mask
)


# ==========================================
# 3. IGNORE AREAS OUTSIDE THE ROAD
# ==========================================

roi_mask = np.zeros((height, width), dtype=np.uint8)

road_roi = np.array([[
    (int(width * 0.05), height - 1),
    (int(width * 0.95), height - 1),
    (int(width * 0.70), int(height * 0.40)),
    (int(width * 0.30), int(height * 0.40))
]], dtype=np.int32)

cv2.fillPoly(roi_mask, road_roi, 255)

lane_mask = cv2.bitwise_and(
    lane_mask, roi_mask
)


# ==========================================
# 4. CONNECT SMALL GAPS
# ==========================================

kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT, (7, 3)
)

lane_mask = cv2.morphologyEx(
    lane_mask, cv2.MORPH_CLOSE, kernel
)


# ==========================================
# 5. MAKE DETECTED MARKINGS RED
# ==========================================

# OpenCV uses BGR colour order:
# Red = (0, 0, 255)
# Green = (0, 255, 0)

red_boundaries = original.copy()
red_boundaries[lane_mask > 0] = (0, 0, 255)


# ==========================================
# 6. SCAN EACH ROW FROM LEFT TO RIGHT
# ==========================================

path_mask = np.zeros(
    (height, width), dtype=np.uint8
)

for y in range(height):

    # True means a lane-marking pixel was detected
    row = lane_mask[y] > 0

    # Find the beginning and end of each continuous
    # group of lane-marking pixels
    changes = np.diff(
        np.concatenate(
            ([False], row, [False])
        ).astype(np.int8)
    )

    starts = np.where(changes == 1)[0]
    ends = np.where(changes == -1)[0]

    # Each continuous group is one detected marking.
    # Fill between marking 1 and 2, then 3 and 4, etc.
    for i in range(0, len(starts) - 1, 2):

        first_boundary = ends[i]
        second_boundary = starts[i + 1]

        # Colour the pixels between the two markings
        if second_boundary > first_boundary:

            path_mask[
                y, first_boundary:second_boundary
            ] = 255


# ==========================================
# 7. COLOUR THE PATH GREEN
# ==========================================

overlay = original.copy()

overlay[path_mask > 0] = (0, 255, 0)

# Make the green transparent
result = cv2.addWeighted(
    overlay, 0.35,
    original, 0.65,
    0
)

# Show detected lane markings in red
result[lane_mask > 0] = (0, 0, 255)


# ==========================================
# 8. DISPLAY RESULTS
# ==========================================

cv2.imshow("Original Image", original)
cv2.imshow("Detected Red Markings", red_boundaries)
cv2.imshow("Lane Mask", lane_mask)
cv2.imshow("Drivable Path - Green", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
