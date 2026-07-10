# Campus Safety AI – Real-Time Fight & Weapon Detection

## Overview

Campus Safety AI is a real-time Computer Vision application developed using Python, OpenCV, and the YOLOv8 object detection model. The system monitors live webcam footage to identify suspicious situations such as physical fights and the presence of weapons. When a potential threat is detected, it displays an alert on the screen and plays an alarm sound.

This project demonstrates how Computer Vision and Artificial Intelligence can be applied to improve safety in schools, colleges, workplaces, and other public environments.

---

## Features

* Real-time webcam monitoring
* Person detection using YOLOv8
* Motion detection using frame differencing
* Basic fight detection based on person proximity and movement
* Weapon alert system (knife/gun detection when supported by the model)
* Audible alarm using Pygame
* Live detection results displayed with bounding boxes

---

## Technologies Used

* Python 3.x
* OpenCV
* Ultralytics YOLOv8
* Pygame

---

## Project Structure

```text
CampusSafetyAI/
│
├── main.py
├── yolov8n.pt
├── alert.wav
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CampusSafetyAI.git
cd CampusSafetyAI
```

### Install dependencies

```bash
pip install ultralytics opencv-python pygame
```

Or install using:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python main.py
```

Make sure:

* A webcam is connected.
* `yolov8n.pt` is present in the project folder.
* `alert.wav` exists in the project folder.

---

## How It Works

1. Captures live video from the webcam.
2. Detects people using the YOLOv8 object detection model.
3. Detects motion by comparing consecutive video frames.
4. Checks whether two detected people are overlapping while significant motion is present.
5. If the condition continues for several frames, the system reports a possible fight.
6. If a supported weapon class is detected, the system immediately raises an alert.
7. An alarm sound is played with a cooldown period to prevent repeated alerts.

---

## Current Limitations

* Fight detection is based on motion and bounding box overlap, so false positives are possible.
* The default YOLOv8 COCO model does not detect weapons such as knives or guns. A custom-trained weapon detection model is required for reliable weapon detection.
* Performance depends on lighting conditions, camera quality, and viewing angle.

---

## Future Improvements

* Train a custom fight detection model using deep learning.
* Integrate a dedicated weapon detection dataset.
* Send Telegram, SMS, or email alerts automatically.
* Store event images and videos for later review.
* Support multiple CCTV cameras simultaneously.
* Improve detection accuracy using pose estimation or action recognition.

---

## Applications

* Educational campuses
* Schools and universities
* Offices and workplaces
* Shopping malls
* Railway stations
* Public surveillance systems

---

## Author

**A. Dhanvanth**

Second-Year Electronics and Communication Engineering (ECE)

Interested in Computer Vision, Artificial Intelligence, Embedded Systems, and Real-Time Safety Applications.
