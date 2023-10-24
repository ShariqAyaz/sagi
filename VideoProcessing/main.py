import cv2

cap = cv2.VideoCapture(0) 

# # Set the video capture properties (if necessary)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set the width of the captured frames
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set the height of the captured frames

output_file = 'captured_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, 30.0, (640, 480))

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    object_only = cv2.bitwise_and(frame, frame, mask=threshold)


    cv2.imshow('Video Capture', object_only)

    #cv2.imshow('Video Capture', frame)
    
    out.write(object_only)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()

cv2.destroyAllWindows()
