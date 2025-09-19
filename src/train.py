# Downloading Dataset

from roboflow import Roboflow
rf = Roboflow(api_key="8W5NJL9PqwOPDLDjAW2q")
project = rf.workspace("mochoye").project("license-plate-detector-ogxxg")
version = project.version(1)
dataset = version.download("yolov8")




# Traning and saving the model

from ultralytics import YOLO

# Initialize YOLOv8 model with pretrained weights
model = YOLO('yolov8m.pt')

# Load custom dataset and train the model
data_path = r"License-Plate-Detector-1\roboflow\data.yaml"
model.train(data=data_path, epochs=100)

# Save the trained model
save_path = "Saved-Yolo-Folder/"
model.save(save_path)