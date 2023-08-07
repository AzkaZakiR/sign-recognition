import cv2

num_cameras = 10  # Check the first 10 camera indices
for i in range(num_cameras):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera {i} is available")
        cap.release()
    else:
        print(f"Camera {i} is not available")
