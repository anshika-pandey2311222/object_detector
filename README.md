🐶🐱 YOLOv8 Object Detector

A mini project that detects objects (like cats, dogs, birds, and more) in images, videos, and webcam streams using YOLOv8.

📌 Features

Detects objects in images

Runs live detection on videos

Works in real-time with webcam feed

Saves output images/videos with bounding boxes

Shows FPS & object counts

🛠️ Tech Stack

Python 3.10+

Ultralytics YOLOv8

OpenCV for image/video handling

PyTorch as the backend

📂 Project Structure
live_detector/
│── detect.py            
│── animal.jpg         
│── requirements.txt    
│── runs/               

⚡ Installation

Clone the repo:

git clone https://github.com/anshika-pandey2311222/yolov8-detector.git
cd yolov8-detector


Create and activate a virtual environment:

python -m venv yolov8-env
yolov8-env\Scripts\activate   


Install dependencies:

pip install -r requirements.txt

🚀 Usage
Detect objects in an image
python detect.py animal.jpg

Detect objects in a video
python detect.py traffic.mp4

Run live webcam detection
python detect.py webcam


👉 Outputs are saved automatically in runs/detect/predict/