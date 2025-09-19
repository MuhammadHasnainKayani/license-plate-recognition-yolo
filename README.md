# License Plate Recognition with YOLO

A computer vision project that detects license plates in images, videos, and live streams using YOLOv8.  
(Optional OCR support with Tesseract can be added to extract text from detected plates.)

---

## 🚀 Features
- Real-time license plate detection using webcam
- Detection from video files
- Detection from a single image
- Batch detection on a folder of images
- Also extraxt the text from the detected plates

---

## 🛠 Tech Stack
- Python 3.8+
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- OpenCV
- (Optional) Tesseract OCR

---

## 📂 Project Structure
```

license-plate-recognition-yolo/
│
├── README.md                <- Project documentation
├── requirements.txt         <- Dependencies
│
├── src/                     <- Source code
│   ├── detect_webcam_plus_text_extraction.py     <- Real-time detection with webcam + Text Extraction
│   ├── detect_video.py      <- Detection on video file
│   ├── detect_batch.py      <- Detection on a folder of images
│   └── train.py             <- Train YOLO on custom dataset


````

---

Install dependencies:

```bash
pip install -r requirements.txt
```


---

## ▶️ Usage

### 1. Real-time detection with webcam

```bash
python src/detect_webcam.py
```

### 2. Detection on a video file

```bash
python src/detect_video.py --video path/to/video.mp4
```


### 3. Batch detection on a folder of images

```bash
python src/detect_batch.py --dir path/to/images/
```

---

## 🏋️ Training on Custom Dataset

To train on your own dataset:

```bash
python src/train.py --data data/data.yaml --epochs 100
```

---
