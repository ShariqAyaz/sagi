import cv2

cap = cv2.VideoCapture(0) 

sift = cv2.SIFT_create()

keypoints_list = []
descriptors_list = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    keypoints, descriptors = sift.detectAndCompute(gray, None)

    keypoints_list.append(keypoints)
    descriptors_list.append(descriptors)

    frame_with_keypoints = cv2.drawKeypoints(frame, keypoints, None)

    cv2.imshow('Frame with Keypoints', frame_with_keypoints)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
