# Face Recognition Attendance System

A Python-based desktop application that uses Face Recognition technology to automatically mark attendance of multiple students using a webcam.

This system detects faces in real time, matches them with stored student images, and records attendance in a CSV file.

---

## 🔹 Features

- Real-time face detection using webcam
- Supports multiple students
- Automatic attendance marking
- Stores attendance in CSV file
- Simple and easy to use
- Desktop based system
- Works offline

---

## 🔹 Technologies Used

- Python 3.10+
- OpenCV
- face_recognition (dlib)
- NumPy
- PIL (Pillow)
- Pandas

---

## 🔹 Project Structure

Face-Recognition-Attendance-System/
│
├── dataset/ # Student images folder
├── trainer.py # Capture student face images
├── recognizer.py # Face recognition + attendance
├── attendance.csv # Attendance record file
├── README.md # Project documentation
└── LICENSE # License file

yaml
Copy code

---

## 🔹 How to Run

### 1️⃣ Install Dependencies

```bash
pip install opencv-python face-recognition numpy pandas pillow
2️⃣ Capture Student Images
bash
Copy code
python trainer.py
Enter student name and press S to capture images.

3️⃣ Run Attendance System
bash
Copy code
python recognizer.py
Webcam will open and attendance will be marked automatically.

🔹 Attendance Format (CSV)
pgsql
Copy code
Name,Date,Time
Rishu_Pathak,2026-01-15,10:45:32
Aman_Shaikh,2026-01-15,10:46:10
🔹 Applications
Colleges & Schools

Offices

Training Institutes

Workshops

Secure Access Systems

🔹 Future Improvements
GUI Interface

Database integration

Cloud storage

Mask detection

Mobile app version

🔹 Author
Rishu Pathak
