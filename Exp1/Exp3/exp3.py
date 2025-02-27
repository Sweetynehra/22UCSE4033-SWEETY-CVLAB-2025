import cv2
import numpy as np
import tkinter as tk
from tkinter import Scale,Frame
from PIL import Image, ImageTk, ImageEnhance

cap = cv2.VideoCapture(0)


root = tk.Tk()
root.title("Webcam Image Adjustments")

# Default values for parameters
contrast_val = tk.DoubleVar(value=1.0)
brightness_val = tk.DoubleVar(value=50)
sharpness_val = tk.DoubleVar(value=1.0)
hue_val = tk.DoubleVar(value=0)
saturation_val = tk.DoubleVar(value=1.0)

main_frame = Frame(root)
main_frame.pack(side="left", padx=5, pady=5)

# Create a label to display the video stream
label = tk.Label(main_frame)
label.pack(side="left", padx=5)

def apply_effects(frame):
    # Convert OpenCV frame to PIL image
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)

    img = ImageEnhance.Contrast(img).enhance(contrast_val.get())
    img = ImageEnhance.Brightness(img).enhance(brightness_val.get() / 50)
    img = ImageEnhance.Sharpness(img).enhance(sharpness_val.get())

    # Convert back to OpenCV format for Hue & Saturation changes
    img_cv = np.array(img)
    img_hsv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2HSV).astype(np.float32)

    img_hsv[..., 0] = (img_hsv[..., 0] + hue_val.get()) % 180  # 0-179

    img_hsv[..., 1] = np.clip(img_hsv[..., 1] * saturation_val.get(), 0, 255)

    # Convert back to RGB
    img_cv = cv2.cvtColor(img_hsv.astype(np.uint8), cv2.COLOR_HSV2RGB)

    return Image.fromarray(img_cv)

def update():
    #Captures frame and updates the GUI with adjusted effects
    ret, frame = cap.read()
    if ret:
        img = apply_effects(frame)
        img_tk = ImageTk.PhotoImage(image=img)
        label.img_tk = img_tk
        label.config(image=img_tk)
    label.after(10, update)  # Refresh every 10ms

# Create sliders for adjustments
def create_slider(name, var, min_val, max_val, row):
    scale = Scale(root, label=name, variable=var, from_=min_val, to=max_val, 
                  resolution=0.1, orient="horizontal", length=200)
    scale.pack()

# Create sliders for each parameter
create_slider("Contrast", contrast_val, 0.1, 3.0, 1)
create_slider("Brightness", brightness_val, 0, 100, 2)
create_slider("Sharpness", sharpness_val, 0.1, 5.0, 3)
create_slider("Hue", hue_val, -50, 50, 4)
create_slider("Saturation", saturation_val, 0.1, 3.0, 5)

# Start updating the GUI
update()

# Run the GUI loop
root.mainloop()

# Release webcam when GUI is closed
cap.release()
cv2.destroyAllWindows()