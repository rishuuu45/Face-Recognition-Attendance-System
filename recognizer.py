import face_recognition
import cv2
import os
from datetime import datetime
import numpy as np
from PIL import Image

dataset = "dataset"
attendance_file = "attendance.csv"

known_faces = []
known_names = []

print("Loading known faces...")

for person in os.listdir(dataset):
    person_path = os.path.join(dataset, person)
    for img_file in os.listdir(person_path):
        img_path = os.path.join(person_path, img_file)

        try:
            pil_img = Image.open(img_path).convert('RGB')  # Ensure RGB
            rgb_img = np.array(pil_img).astype(np.uint8)  # Ensure uint8
        except Exception as e:
            print(f"Skipping {img_path} due to PIL error: {e}")
            continue

        encodings = face_recognition.face_encodings(rgb_img)
        if len(encodings) == 0:
            print(f"No face found in: {img_path}")
            continue

        known_faces.append(encodings[0])
        known_names.append(person)

print(f"Loaded {len(known_faces)} faces.")

cam = cv2.VideoCapture(0)
marked = []

print("Starting webcam... Press ESC to exit")

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).astype(np.uint8)

    faces = face_recognition.face_locations(rgb_frame)
    encodes = face_recognition.face_encodings(rgb_frame, faces)

    for encode, loc in zip(encodes, faces):
        matches = face_recognition.compare_faces(known_faces, encode)
        name = "Unknown"

        if True in matches:
            name = known_names[matches.index(True)]

        if name != "Unknown" and name not in marked:
            marked.append(name)
            now = datetime.now()
            with open(attendance_file, "a") as f:
                f.write(f"{name},{now.date()},{now.strftime('%H:%M:%S')}\n")
            print(f"Attendance marked for {name}")

        y1, x2, y2, x1 = loc
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, name, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Attendance", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
print("Webcam closed. Attendance recording finished.")




