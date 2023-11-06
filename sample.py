from sketchpy import canvas
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tempfile
import os
import cv2
import svgwrite

#def convert_to_svg(input_path, output_path):
    # Read the JPG image
 #   img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply edge detection (Canny)
  #  edges = cv2.Canny(img, 30, 100)
    
    # Find contours in the edge-detected image
   # contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # SVG File Initialization:
    #dwg = svgwrite.Drawing(output_path, size=(img.shape[1], img.shape[0]))

    # Write SVG Path Data:
    #for contour in contours:
     #   points = [tuple(map(float, point[0])) for point in contour]
      #  dwg.add(dwg.polygon(points, fill="black"))

    # Save the SVG file
    #dwg.save()

def upload_file():
    global img_label
    f_types = [('svg Files', '*.svg'), ('jpeg Files', '*.jpeg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    
    # Convert JPG to SVG
    temp_svg_path = os.path.join(tempfile.gettempdir(), "temp_image.svg")
   # convert_to_svg(filename, temp_svg_path)

    # Display the SVG
    obj = canvas.sketch_from_svg(filename,scale=70)
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
