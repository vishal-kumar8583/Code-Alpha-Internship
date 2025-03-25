# Code-Alpha-Internship
CodeAlpha-Task-3-Object Detection and Tracking
This repository contains a Python script that utilizes the YOLO (You Only Look Once) model for object tracking in a video stream using OpenCV. The script reads a video file, detects and tracks objects, and displays the results in a dynamically resized window.

Features
YOLOv8 Model: Utilizes the YOLOv8 model for object detection and tracking.
Video Processing: Reads and processes video frames in real-time.
Dynamic Resizing: Resizes the output window to fit the screen for better visualization.
Object Tracking: Detects and tracks objects in each frame of the video.
Requirements
Python 3.x
OpenCV
Ultralytics YOLO
Installation

cd yolo-object-tracking
Create a virtual environment:

pip install pipenv
pipenv shell
Usage
Download the YOLOv8 model weights:
Download the yolov8n.pt weights file from the official YOLO repository or another trusted source and place it in the project directory.

Place your video file:
Place the video file you want to process (e.g., test2.mp4) in the project directory.

Run the script:

python yolo_object_tracking.py

Script Details
The yolo_object_tracking.py script:

Loads the YOLOv8 model. Opens the video file specified. Reads and processes each frame of the video. Detects and tracks objects using the YOLO model. Plots the detection results. Resizes the frame for better visualization. Displays the processed frames in a dynamically resized window.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Ultralytics for the YOLO model and weights. OpenCV for the computer vision library.

Contact
For any questions or suggestions, please open an issue or contact your-email@example.com.
