from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import os
import sys

root=Tk()
root.geometry("1000x600")
root.configure(background='#323846')

file_path=''

def set_file_path(path):
    global file_path
    file_path=path

def open_file():
    path=askopenfilename(filetypes=[('Python Files','*.py')])
    if path:
        with open(path,'r') as file:
            code=file.read()
            input.delete('1.0',END)
            input.insert('1.0',code)
            set_file_path(path)


def save_file():
    if file_path=='':
        path=asksaveasfilename(filetypes=[('Python Files','*.py')])
        if not path:
            return
    else:
        path=file_path
 
    with open(path,'w') as file:
        code=input.get('1.0',END)
        file.write(code)
        set_file_path(path)

def run_file():
    if file_path=='':
        messagebox.showerror("Python IDLE",'Save Your Code')
        return
    print(file_path)
    command = f'"{sys.executable}" "{file_path}"'
    process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    result,error=process.communicate()
    output.delete('1.0', END)  # Clear the output box before inserting new output
    output.insert('1.0', result.decode())  # Insert the standard output
    output.insert('1.0', error.decode())
img = Image.open("assests/new.jpg")
imgT = Image.open("assests/save.jpg")
img2 = Image.open("assests/run.jpg")
photo=ImageTk.PhotoImage(img)
photo2=ImageTk.PhotoImage(img2)
photoT=ImageTk.PhotoImage(imgT)

Button(root,image=photo,width=85,bd=0,highlightthickness=0,bg='#323846',command=open_file).place(x=20,rely=0.1)
Button(root,image=photoT,width=85,bd=0,highlightthickness=0,bg='#323846',command=save_file).place(x=20,rely=0.3)
Button(root,image=photo2,width=85,bd=0,highlightthickness=0,bg='#323846',command=run_file).place(x=20,rely=0.5)
input=Text(root,background='white',width=46,font='Ariels 15 bold')
input.place(relx=0.15,y=20)
output=Text(root,background='#323846',width=40,font='Ariels 15 bold',foreground='white')
output.place(relx=0.6,y=20)


root.mainloop()