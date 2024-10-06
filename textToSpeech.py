import tkinter as tk
import pyttsx3
from tkinter import filedialog
import os

root=tk.Tk()
root.geometry("1000x600")
root.configure(background='black')

engine = pyttsx3.init()

def speakNow():
    text=text_area.get(1.0,'end').strip()
    gender=selected_option.get()
    speed=selected_option2.get()
    voices=engine.getProperty("voices")

    def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()


def download():
     text=text_area.get(1.0,'end').strip()
     gender=selected_option.get()
     speed=selected_option2.get()
     voices=engine.getProperty("voices")

     def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()

     if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()


tk.Label(root,background="white",height=4,text='Text To Speech',font='Ariels 20 bold').pack(fill=tk.X)
f1=tk.Frame(root,bg="#000080",height=700)
f1.pack(fill=tk.X)
text_area=tk.Text(f1,background='white',width='30',font='Ariels 25 bold')
text_area.place(x=10,y=15)

tk.Label(f1,text='VOICE',font='Ariels 15 bold',background='#000080',fg='white').place(relx=0.6,y=40)
selected_option = tk.StringVar(f1)
selected_option.set("Male")  # Default value

# Create OptionMenu
options = ["Male", "Female"]
option_menu = tk.OptionMenu(f1, selected_option, *options)
option_menu.config(width=14)
option_menu.place(relx=0.6,y=80)

tk.Label(f1,text='SPEED',font='Ariels 15 bold',background='#000080',fg='white').place(relx=0.8,y=40)
selected_option2 = tk.StringVar(f1)
selected_option2.set("Normal")  # Default value

# Create OptionMenu
options2 = ["Fast", "Normal", "Slow"]
option_menu2 = tk.OptionMenu(f1, selected_option2, *options2)
option_menu2.config(width=14)
option_menu2.place(relx=0.8,y=80)

tk.Button(f1,text='Speak',font='Ariels 14 bold',command=speakNow).place(relx=0.6,rely=0.4)
tk.Button(f1,text='Save',font='Ariels 14 bold',background='green',fg='black',command=download).place(relx=0.8,rely=0.4)

root.mainloop()