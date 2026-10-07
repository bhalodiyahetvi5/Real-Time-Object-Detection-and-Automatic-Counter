# 📷 Accurate Real-Time Object Detection & Automatic Counter

An end-to-end Computer Vision application built with Python, YOLOv8, and OpenCV to detect and count all objects accurately in real-time via webcam stream.

---

## 📌 Project Overview
- **Objective:** Detect multiple objects in real-time with high accuracy and maintain a dynamic live count on screen.
- **Model:** YOLOv8 Medium (`yolov8m.pt`) for balanced speed and superior detection accuracy.
- **Tech Stack:** Python, Ultralytics YOLOv8, OpenCV.

---

## 🛠️ Features
- **Accurate Detection:** Leverages confidence thresholding (`conf=0.55`) and IoU optimization (`iou=0.45`) to eliminate false detections and duplicate boxes.
- **Real-Time Counting:** Automatically calculates total objects detected per frame and renders an overlay banner.
- **Multi-Class Support:** Detects various everyday classes (e.g., person, cell phone, laptop, bottle, chair).

---

