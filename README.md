# 🐦 Object Detector (YOLOv8)

A real-time object detection project using **YOLOv8**.  
Detect objects from **images, videos, and webcam streams** with high accuracy.

---

## ⚡ Features
- Detects multiple objects in images, videos, and live webcam feeds.  
- Built with **Ultralytics YOLOv8**.  
- Lightweight, fast, and easy to run.  

---

## 📂 Project Structure
├── detect.py 
├── animal.jpg # Sample image
├── bus.jpg # Sample image
├── traffic.mp4 # Sample video
└── README.md 


---

## ⚙️ Installation
```bash
# Clone this repository
git clone https://github.com/anshika-pandey2311222/object_detector.git
cd object_detector

# Create virtual environment
python -m venv yolov8-env
yolov8-env\Scripts\activate   # On Windows

# Install dependencies
pip install ultralytics opencv-python

🚀 Usage
🖼️ Run detection on an Image:
python detect.py animal.jpg

🎥 Run detection on a Video:
python detect.py traffic.mp4

📷 Run detection on Webcam:
python detect.py 0