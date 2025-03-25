import cv2
import torch
import numpy as np
from ultralytics import YOLO

# Load the YOLOv8 model
yolo_model = YOLO("yolov8n.pt")  # Using a pre-trained YOLOv8 model

def detect_and_track_objects(video_source=0):
    """Detect and track objects in real-time using YOLOv8."""
    cap = cv2.VideoCapture(video_source)
    
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Run YOLO detection on the frame
        results = yolo_model(frame)
        
        # Draw bounding boxes and labels
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = box.conf[0].item()
                cls = int(box.cls[0].item())
                label = f"{yolo_model.names[cls]}: {conf:.2f}"
                
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        cv2.imshow("Object Detection & Tracking", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_and_track_objects()
