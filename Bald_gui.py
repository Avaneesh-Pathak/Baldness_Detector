import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import random

def detect_baldness():
    # Simulate a random detection result
    is_bald = random.choice([True, False])

    if is_bald:
        result_label.config(text="Baldness detected!")
    else:
        result_label.config(text="No baldness detected.")

def browse_image():
    # Open file dialog to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])

    if file_path:
        # Open the selected image file
        image = Image.open(file_path)
        # Resize the image to fit the display area
        image = image.resize((300, 300))
        # Convert the image to Tkinter format
        photo = ImageTk.PhotoImage(image)

        # Display the image on the GUI
        image_label.config(image=photo)
        image_label.image = photo

# Create the main window
window = tk.Tk()
window.title("Baldness Detection")

# Create the image label
image_label = tk.Label(window)
image_label.pack(pady=10)

# Create the buttons
browse_button = tk.Button(window, text="Browse Image", command=browse_image)
browse_button.pack(pady=5)

detect_button = tk.Button(window, text="Detect Baldness", command=detect_baldness)
detect_button.pack(pady=5)

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run the GUI main loop
window.mainloop()
