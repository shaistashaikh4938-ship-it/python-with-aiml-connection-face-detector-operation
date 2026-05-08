import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Camera start
cap = cv2.VideoCapture(0)

# GUI
window = tk.Tk()
window.title("Face Detector")
window.geometry("700x600")

label = tk.Label(window)
label.pack()

def detect_face():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.3, minNeighbors=5
        )

        # Draw rectangle on faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Convert image for Tkinter
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)

        label.imgtk = imgtk
        label.configure(image=imgtk)

    label.after(10, detect_face)

# Start button
btn = tk.Button(window, text="Start Camera", command=detect_face)
btn.pack(pady=10)

# Exit button
def close():
    cap.release()
    window.destroy()

exit_btn = tk.Button(window, text="Exit", command=close)
exit_btn.pack(pady=10)

window.mainloop()
