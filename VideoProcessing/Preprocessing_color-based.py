import cv2
import numpy as np

cap = cv2.VideoCapture(0)

output_file = 'captured_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, 30.0, (640, 480))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper thresholds for the white color range
    lower_white = np.array([0, 0, 100], dtype=np.uint8)
    upper_white = np.array([180, 30, 255], dtype=np.uint8)

    # Create a mask based on the white color range
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Bitwise AND operation to extract the object from the frame
    object_only = cv2.bitwise_and(frame, frame, mask=mask)

    # Show the object in the original shape and color
    cv2.imshow('Object Only Stream', object_only)

    out.write(object_only)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()

cv2.destroyAllWindows()
