
from sketchpy import canvas
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tempfile
import os


def upload_file():
    global img_label
    f_types = [('Jpg Files', '*.jpg'),('jpeg Files','*.jpeg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)

    # Save the image to a temporary file
    temp_file_path = os.path.join(tempfile.gettempdir(), "temp_image.jpg")
    img.save(temp_file_path)


    # Display the image
    # img = ImageTk.PhotoImage(img)
    # img_label.config(image=img)
    # img_label.image = img

    # Create a sketch from the temporary file
    obj = canvas.sketch_from_image(temp_file_path)
    obj.draw()


my_w = tk.Tk()
my_w.geometry("400x400")  # Adjusted the window size
my_w.title('Turtle')
my_font1 = ('times', 18, 'bold')

l1 = tk.Label(my_w, text='Select Photo', width=30, font=my_font1)
l1.grid(row=1, column=1)

b1 = tk.Button(my_w, text='Upload File', width=20, command=upload_file)
b1.grid(row=2, column=1)

img_label = tk.Label(my_w)
img_label.grid(row=3, column=1)

my_w.mainloop()

