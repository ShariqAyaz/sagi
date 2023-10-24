import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Use the appropriate camera index if multiple cameras are connected

white_hair_image = cv2.imread('white_hair.png')  # Load the white hair image with transparent background

# If the white hair image has no transparency, create a mask using white pixels
white_hair_mask = np.zeros_like(white_hair_image[:, :, 0])
white_hair_mask[white_hair_image[:, :, 0] == 255] = 255

overlay_alpha = 0.5  # Set the transparency level of the white hair overlay

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Resize the white hair image or mask to match the size of the frame
    white_hair_overlay = cv2.resize(white_hair_image, (frame.shape[1], frame.shape[0]))
    white_hair_mask_resized = cv2.resize(white_hair_mask, (frame.shape[1], frame.shape[0]))

    # Apply the white hair overlay using the mask
    frame_with_white_hair = cv2.addWeighted(frame, 1.0 - overlay_alpha, white_hair_overlay, overlay_alpha, 0)
    frame_with_white_hair[np.where(white_hair_mask_resized == 255)] = white_hair_overlay[np.where(white_hair_mask_resized == 255)]

    # Display the processed frame
    cv2.imshow('White Hair Video', frame_with_white_hair)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
