import cv2
from ultralytics import YOLO

# Load YOLOv8 model with trained weights
model = YOLO("Yolo_finetuned_model/weights/best.pt")

# Path to input video file
video_path = r"C:\Users\muham\Downloads\Video\2103099-uhd_3840_2160_30fps.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    results = model(frame)

    # Draw bounding boxes and labels
    annotated_frame = results[0].plot()

    # Show annotated video
    cv2.imshow("License Plate Detection", annotated_frame)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
