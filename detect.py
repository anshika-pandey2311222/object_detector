import argparse
import cv2
import time
from collections import Counter
from ultralytics import YOLO

def detect_source(model_path, source):
    model = YOLO(model_path)

    if source == "webcam":
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not access webcam")
            return
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            start_time = time.time()
            results = model(frame, stream=True)

            object_names = []
            for r in results:
                frame = r.plot() 
                for c in r.boxes.cls:
                    object_names.append(model.names[int(c)])

            counts = Counter(object_names)
            fps = 1 / (time.time() - start_time)

            info_text = f"FPS: {fps:.2f} | " + ", ".join([f"{k}: {v}" for k, v in counts.items()])
            cv2.putText(frame, info_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (0, 255, 0), 2)

            cv2.imshow("YOLOv8 Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()

    else:
        results = model(source, save=True, stream=True)
        object_names = []
        for r in results:
            for c in r.boxes.cls:
                object_names.append(model.names[int(c)])
        
        counts = Counter(object_names)
        print("✅ Detection complete.")
        print("Detected objects:", dict(counts))
        print("Results saved to:", results[0].save_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv8 Object Detection")
    parser.add_argument("--model", type=str, default="yolov8n.pt",
                        help="YOLO model (yolov8n.pt, yolov8s.pt, etc.)")
    parser.add_argument("--source", type=str, required=True,
                        help="Image/Video path or 'webcam'")
    args = parser.parse_args()

    detect_source(args.model, args.source)
