import cv2
import os
from PIL import Image
import numpy as np

# Student name input
name = input("Enter Student Name: ")
name = name.replace(" ", "_")  # Space-safe
path = os.path.join("dataset", name)

if not os.path.exists(path):
    os.makedirs(path)

cam = cv2.VideoCapture(0)
count = 0

print("Press 'S' to capture image, ESC to exit")

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Capture Face - Press S to save", frame)
    key = cv2.waitKey(1)

    if key == ord('s'):
        count += 1
        # Convert BGR → RGB + dtype uint8
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).astype(np.uint8)
        pil_img = Image.fromarray(rgb_frame)
        # Save as JPG
        pil_img.save(os.path.join(path, f"{count}.jpg"), "JPEG", quality=95)
        print(f"Image {count} saved")
    elif key == 27:  # ESC
        break

    if count == 20:
        break

cam.release()
cv2.destroyAllWindows()
print(f"Captured {count} images for {name}")