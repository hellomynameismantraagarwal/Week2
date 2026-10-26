import cv2
import numpy as np

def findcont(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    contours, _= cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0,0,255), 2)
    return image


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

print("Camera feed started. Press 'q' to quit.")

while True:
    # Capture frame-by-frame
    # 'ret' is a boolean (True if frame read successfully, False if not)
    # 'frame' is the actual image array
    ret, frame = cap.read()

    # If the frame wasn't grabbed properly, break the loop
    if not ret:
        print("Error: Can't receive frame. Exiting...")
        break
    frame = findcont(frame)
    cv2.imshow('Live Camera Feed', frame)

    # Wait for 1 millisecond and check if the user pressed the 'q' key
    # 0xFF masks the keypress to work reliably across different operating systems
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the camera capture and close all windows
cap.release()
cv2.destroyAllWindows()
