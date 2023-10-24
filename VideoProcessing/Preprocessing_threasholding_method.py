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
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to create a binary mask
    _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    
    # Bitwise AND operation to extract the object from the frame
    object_only = cv2.bitwise_and(frame, frame, mask=threshold)
    
    # Show the original frame in a separate window
    cv2.imshow('Original Stream', frame)
    
    # Show the object-only stream in the main window
    cv2.imshow('Object Only Stream', object_only)
    
    out.write(object_only)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()

cv2.destroyAllWindows()
