import tkinter as tk
from tkinter import messagebox
import os

# Functions for buttons
def register():
    os.system("python trainer.py")  # Opens student registration

def recognize():
    os.system("python recognizer.py")  # Starts attendance recognition

# GUI window
root = tk.Tk()
root.title("Face Recognition Attendance System")
root.geometry("400x300")  # Width x Height

tk.Label(root, text="Face Attendance System", font=("Arial", 20)).pack(pady=20)

tk.Button(root, text="Register Student", width=20, command=register).pack(pady=10)
tk.Button(root, text="Start Attendance", width=20, command=recognize).pack(pady=10)
tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=10)

root.mainloop()
