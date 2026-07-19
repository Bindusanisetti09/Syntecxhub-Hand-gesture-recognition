# ✋ Hand Gesture Recognition System

A real-time **Hand Gesture Recognition System** built using **Python, OpenCV, and MediaPipe**.  
The project detects hand landmarks from a webcam, recognizes gestures, provides voice feedback, captures screenshots, and stores gesture history in a CSV file.

---

## 📌 Features

- 🎥 Real-time webcam hand tracking
- 🖐 Detects multiple hand gestures
- 🔊 Voice feedback using Text-to-Speech
- 📸 Screenshot capture using gestures
- 📝 Gesture history logging in CSV
- ⚡ FPS (Frames Per Second) display
- 🧩 Modular Python project structure

---

## 🛠 Technologies Used

- **Python 3.11**
- **OpenCV**
- **MediaPipe**
- **NumPy**
- **Pandas**
- **pyttsx3**

---

## 📂 Project Structure

```text
HAND_GESTURE_RECOGNITION/
│── main.py
│── hand_detector.py
│── gesture_classifier.py
│── gesture_actions.py
│── camera.py
│── settings.py
│── utils.py
│── voice.py
│── logger.py
│── screenshots.py
│── requirements.txt
│── README.md
│── data/
│    └── history.csv
│── screenshots/
