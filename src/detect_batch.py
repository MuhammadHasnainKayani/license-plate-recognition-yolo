import cv2
import os
from ultralytics import YOLO

# Load YOLOv8 model with trained weights
model = YOLO("Yolo_finetuned_model/weights/best.pt")

# Directory containing test images
images_directory = "yolo_test_images"

# Fixed display dimensions
frame_width = 400
frame_height = 400

# Iterate over all images in the directory
for filename in os.listdir(images_directory):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(images_directory, filename)
        image = cv2.imread(image_path)

        # Perform object detection
        results = model(image)

        # Draw bounding boxes and labels
        annotated_image = results[0].plot()
        annotated_image = cv2.resize(annotated_image, (frame_width, frame_height))

        # Show result
        cv2.imshow("License Plate Detection", annotated_image)

        # Press 'q' to move to next image
        if cv2.waitKey(0) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
