# AirMouse

A real-time gesture-controlled virtual mouse built using Computer Vision and Hand Tracking.
AirMouse enables users to control their computer using hand gestures captured through a webcam, eliminating the need for a physical mouse. The project combines real-time hand landmark detection, gesture recognition, and desktop automation to create a touchless Human-Computer Interaction system.

---

# Features

- Real-time hand tracking using webcam 
- Cursor movement using index finger  
- Left click using thumb-index pinch gesture  
- Scroll up using open palm gesture  
- Scroll down using back-of-hand gesture  
- Smooth and responsive interaction  
- Live gesture visualization and debugging  

---

# Gestures

| Gesture | Action |
|---|---|
| ☝️ Index Finger | Move Cursor |
| 🤏 Thumb + Index Pinch | Left Click |
| ✋ Open Palm | Scroll Up |
| 🤚 Back of Hand | Scroll Down |
| ESC Key | Exit Application |

---

# Tech Stack

- Python
- OpenCV
- MediaPipe
- PyAutoGUI

---

# Concepts Used

- Computer Vision
- Hand Landmark Detection
- Gesture Recognition
- Human-Computer Interaction (HCI)
- Real-Time Tracking
- Desktop Automation

---

# How It Works

The system captures live video from the webcam and processes each frame using MediaPipe Hands.
The workflow:

1. Detect hand landmarks
2. Identify finger positions
3. Recognize gestures
4. Map gestures to mouse operations
5. Execute actions using PyAutoGUI

---

# Project Architecture

```bash
Smart-AirMouse/
│
├── virtual_mouse.py
├── requirements.txt
└── README.md
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/vismayaunnik/airmouse.git
```

---

## Navigate to the Project Folder

```bash
cd airmouse
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python virtual_mouse.py
```

---

# Requirements

Create a `requirements.txt` file containing:

```txt
opencv-python
mediapipe
pyautogui
```

---

# Challenges Faced

- Gesture overlap causing unintended actions
- Click gesture stability
- Scroll sensitivity tuning
- Real-time tracking optimization
- Hand orientation detection

---

# Future Improvements

- Right-click gesture
- Drag and drop support
- Volume and brightness control
- Gesture customization
- Multi-hand tracking
- AI-based gesture classification
- Virtual keyboard integration

---

