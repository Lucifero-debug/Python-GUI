from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

root = Tk()
root.geometry("800x520")
root.config(bg="#f2f3f5")

current_x = 0
current_y = 0
color = 'black'
f_img = None
image_on_canvas = None
original_img = None
resizing = False
filename = None  # Declare filename at the top

def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y

def addline(work):
    global current_x, current_y
    canvas.create_line((current_x, current_y, work.x, work.y), width=get_current_value(), fill=color, capstyle=ROUND, smooth=True)
    current_x, current_y = work.x, work.y

def show_color(new_color):
    global color
    color = new_color

def new_canvas():
    canvas.delete('all')
    display_pallete()

def insertImage():
    global filename, f_img, original_img, image_on_canvas
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetype=(("PNG file", "*.png"), ("All files", "*.*")))
    
    if filename:  # Ensure a file is selected
        original_img = Image.open(filename)  # Store original image for resizing
        resized_img = original_img.resize((200, 200))  # Default initial size
        f_img = ImageTk.PhotoImage(resized_img)  # Convert to Tkinter-compatible format
        image_on_canvas = canvas.create_image(180, 50, image=f_img, anchor=NW)  # Place image on canvas

        canvas.image = f_img  # Keep reference to prevent GC

# Initialize these globals to store the initial size during resize
initial_width = 0
initial_height = 0

def start_resize(event):
    global resizing, current_x, current_y, initial_width, initial_height
    # Check if click is inside the image bounds
    if image_on_canvas is not None:
        bbox = canvas.bbox(image_on_canvas)
        if bbox[0] <= event.x <= bbox[2] and bbox[1] <= event.y <= bbox[3]:
            resizing = True
            current_x, current_y = event.x, event.y
            
            # Store the current dimensions of the image for calculating new size
            initial_width = canvas.bbox(image_on_canvas)[2] - canvas.bbox(image_on_canvas)[0]
            initial_height = canvas.bbox(image_on_canvas)[3] - canvas.bbox(image_on_canvas)[1]

def do_resize(event):
    global f_img, image_on_canvas, original_img, resizing, current_x, current_y, initial_width, initial_height

    if resizing and original_img:  # Check if resizing is enabled
        # Calculate the change in mouse position
        width_change = event.x - current_x
        height_change = event.y - current_y

        # New dimensions based on initial size and mouse movement
        new_width = max(50, initial_width + width_change)
        new_height = max(50, initial_height + height_change)

        # Resize the image and update it on the canvas
        resized_img = original_img.resize((new_width, new_height))
        f_img = ImageTk.PhotoImage(resized_img)
        canvas.itemconfig(image_on_canvas, image=f_img)

        # Update current_x and current_y to the new mouse position
        current_x, current_y = event.x, event.y

# Reset the resizing state when the mouse is released
def stop_resize(event):
    global resizing
    resizing = False  # Stop resizing when mouse is released
# Initialize these globals to store the initial size during resize
initial_width = 0
initial_height = 0

def start_resize(event):
    global resizing, current_x, current_y, initial_width, initial_height
    # Check if click is inside the image bounds
    if image_on_canvas is not None:
        bbox = canvas.bbox(image_on_canvas)
        if bbox[0] <= event.x <= bbox[2] and bbox[1] <= event.y <= bbox[3]:
            resizing = True
            current_x, current_y = event.x, event.y
            
            # Store the current dimensions of the image for calculating new size
            initial_width = canvas.bbox(image_on_canvas)[2] - canvas.bbox(image_on_canvas)[0]
            initial_height = canvas.bbox(image_on_canvas)[3] - canvas.bbox(image_on_canvas)[1]

def do_resize(event):
    global f_img, image_on_canvas, original_img, resizing, current_x, current_y, initial_width, initial_height

    if resizing and original_img:  # Check if resizing is enabled
        # Calculate the change in mouse position
        width_change = event.x - current_x
        height_change = event.y - current_y

        # New dimensions based on initial size and mouse movement
        new_width = max(50, initial_width + width_change)
        new_height = max(50, initial_height + height_change)

        # Resize the image and update it on the canvas
        resized_img = original_img.resize((new_width, new_height))
        f_img = ImageTk.PhotoImage(resized_img)
        canvas.itemconfig(image_on_canvas, image=f_img)

        # Update current_x and current_y to the new mouse position
        current_x, current_y = event.x, event.y

# Reset the resizing state when the mouse is released
def stop_resize(event):
    global resizing
    resizing = False  # Stop resizing when mouse is released
# Initialize these globals to store the initial size during resize
initial_width = 0
initial_height = 0

def start_resize(event):
    global resizing, current_x, current_y, initial_width, initial_height
    # Check if click is inside the image bounds
    if image_on_canvas is not None:
        bbox = canvas.bbox(image_on_canvas)
        if bbox[0] <= event.x <= bbox[2] and bbox[1] <= event.y <= bbox[3]:
            resizing = True
            current_x, current_y = event.x, event.y
            
            # Store the current dimensions of the image for calculating new size
            initial_width = canvas.bbox(image_on_canvas)[2] - canvas.bbox(image_on_canvas)[0]
            initial_height = canvas.bbox(image_on_canvas)[3] - canvas.bbox(image_on_canvas)[1]

def do_resize(event):
    global f_img, image_on_canvas, original_img, resizing, current_x, current_y, initial_width, initial_height

    if resizing and original_img:  # Check if resizing is enabled
        # Calculate the change in mouse position
        width_change = event.x - current_x
        height_change = event.y - current_y

        # New dimensions based on initial size and mouse movement
        new_width = max(50, initial_width + width_change)
        new_height = max(50, initial_height + height_change)

        # Resize the image and update it on the canvas
        resized_img = original_img.resize((new_width, new_height))
        f_img = ImageTk.PhotoImage(resized_img)
        canvas.itemconfig(image_on_canvas, image=f_img)

        # Update current_x and current_y to the new mouse position
        current_x, current_y = event.x, event.y

# Reset the resizing state when the mouse is released
def stop_resize(event):
    global resizing
    resizing = False  # Stop resizing when mouse is released
 # Stop resizing when mouse is released


def erase():
    pass

img = Image.open("assests/color.jpg")
img2 = Image.open("assests/eraser.jpg")
img3 = Image.open("assests/add.jpg")
img4 = Image.open("assests/image.jpeg")
img4 = img4.resize((30, 30))

photo = ImageTk.PhotoImage(img)
photo2 = ImageTk.PhotoImage(img2)
photo3 = ImageTk.PhotoImage(img3)
photo4 = ImageTk.PhotoImage(img4)

Label(root, image=photo, bg='#f2f3f5').place(x=10, y=20)
Button(root, image=photo2, bg='#f2f3f5', command=erase).place(x=30, y=370)
Button(root, image=photo3, bg='white', command=new_canvas).place(x=30, y=410)
Button(root, image=photo4, bg='white', command=insertImage).place(x=30, y=450)

colors = Canvas(root, bg='#fff', width=37, height=300, bd=0)
colors.place(x=30, y=60)

def display_pallete():
    id = colors.create_rectangle((10, 10, 30, 30), fill='black')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))
    
    id = colors.create_rectangle((10, 40, 30, 60), fill='gray')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))

    id = colors.create_rectangle((10, 70, 30, 90), fill='brown')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown'))

    id = colors.create_rectangle((10, 100, 30, 120), fill='red')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

    id = colors.create_rectangle((10, 130, 30, 150), fill='orange')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

    id = colors.create_rectangle((10, 160, 30, 180), fill='yellow')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

    id = colors.create_rectangle((10, 190, 30, 210), fill='green')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

    id = colors.create_rectangle((10, 220, 30, 240), fill='blue')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

    id = colors.create_rectangle((10, 250, 30, 270), fill='purple')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))

display_pallete()

# Main screen
canvas = Canvas(root, width=930, height=500, background='white', cursor='hand2')
canvas.place(x=100, y=10)

# Bind drawing events to the left mouse button (Button-1)
canvas.bind('<Button-1>', locate_xy)  # Get starting point for drawing
canvas.bind('<B1-Motion>', addline)     # Draw line while moving

# Bind resizing events to the right mouse button (Button-3)
canvas.bind('<Button-3>', start_resize)  # Start resizing on right-click
canvas.bind('<B3-Motion>', do_resize)     # Resize the image while dragging
canvas.bind('<ButtonRelease-3>', stop_resize)  # Stop resizing on mouse release

current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())  # Corrected to call the function

slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=slider_changed, variable=current_value)
slider.place(x=30, y=500)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=550)

root.mainloop()
