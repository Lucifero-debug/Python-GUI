from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfile
import tkinter.simpledialog as sd

root=Tk()
root.geometry("422x320")

root.config(background="white")

var=StringVar()
var.set("")
filevalue = StringVar()

def newFile():
    a=tmsg.askquestion("Warning!","Do you want to save the current file?")
    if a=="yes":
        with open(f"{filevalue.get()}.txt",'w') as f:
            f.write(f"{var.get()}")
        text_area.delete(1.0,END)
        filevalue.set("")

def openFile():
     file_name = sd.askstring("Open", "Enter the file name:")
     try:
        with open(f"{file_name}.txt",'r') as f:
            content=f.read()
            text_area.delete(1.0,END)
            text_area.insert(1.0,content)
            filevalue.set(file_name)
     except Exception as e:
         tmsg.showerror("Error", f"An error occurred: {str(e)}")
     except FileNotFoundError:
            tmsg.showerror("Error", "File not found.")  
         

def saveFile():
    with open(f"{filevalue.get()}.txt",'w') as f:
      f.write(f"{var.get()}")
    var.set("")
    text_area.delete(1.0,END)
    filevalue.set("")
def cutFile():
    text_area.event_generate("<<Cut>>")
def copyFile():
    text_area.event_generate("<<Copy>>")
def pasteFile():
    text_area.event_generate("<<Paste>>")

def on_type(event):
    var.set(text_area.get(1.0,END))
    print(var.get())

fileentry = Entry(root,textvariable=filevalue)
fileentry.pack()
yourmenu=Menu(root)
m1=Menu(yourmenu,tearoff=0)
m1.add_command(label="New",command=newFile)
m1.add_command(label="Open",command=openFile)
m1.add_command(label="Save",command=saveFile)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="File",menu=m1)

m2=Menu(yourmenu,tearoff=0)
m2.add_command(label="Cut",command=cutFile)
m2.add_command(label="Copy",command=copyFile)
m2.add_command(label="Paste",command=pasteFile)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="Edit",menu=m2)

text_area = Text(root, wrap='word', undo=True, font=("Arial", 12))
text_area.pack(expand=1, fill=BOTH)

# Add a vertical scrollbar
scrollbar = Scrollbar(text_area)
scrollbar.pack(side=RIGHT, fill=Y)

# Attach the scrollbar to the Text widget
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)
text_area.bind('<KeyRelease>', on_type)



root.mainloop()