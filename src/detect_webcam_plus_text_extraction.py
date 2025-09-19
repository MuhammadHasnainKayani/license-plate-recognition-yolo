
import cv2
from ultralytics import YOLO
import pytesseract

detected_plates_list=[]
# Load the YOLOv8 model with the trained weights
model = YOLO("Yolo_finetuned_model/weights/best.pt")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# # Open the video file
# video_path = r"C:\Users\muham\Downloads\Video\2103099-uhd_3840_2160_30fps.mp4"
# cap = cv2.VideoCapture(video_path)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# Loop to continuously capture frames from the webcam
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if not ret:
        print("Error: Could not read frame")
        break

    # Perform object detection on the frame
    results = model(frame)

    # Draw bounding boxes and labels on the frame
    annotated_frame = results[0].plot()
    best_text = ""
    best_confidence = 0.5

    for result in results:
        for detection, conf in zip(result.boxes.xyxy, result.boxes.conf):
            x1, y1, x2, y2 = detection

            plate_img = frame[int(y1):int(y2), int(x1):int(x2)]

            # Apply preprocessing techniques to enhance the plate image
            gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (3, 3), 0)
            thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
            plate_text = pytesseract.image_to_string(plate_img, config='--psm 11')

            # Check if the text is clearer than the current best text
            if conf > best_confidence:
                detected_plates_list.append(plate_text)
                print("License Plate Text:", plate_text)

    print("Best License Plate Text:", best_text)
    # Display the annotated frame
    cv2.imshow('Object Detection', annotated_frame)

    # Wait for 'q' key to quit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

print(list)

