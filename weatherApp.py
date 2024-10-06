from tkinter import *
from PIL import Image, ImageTk
import requests
from datetime import datetime, timedelta

def fetch_random_quotes_freeapi():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={entry.get()}&appid=d3493edaf2e84e9bc4ece1c52569434d&units=metric"
    response = requests.get(url)
    data = response.json()
    print(data)
    wind_label.config(text=data['wind']['speed'])
    humidity_label.config(text=data['main']['humidity'])
    pressure_label.config(text=data['main']['pressure'])
    description_label.config(text=data['weather'][0]['description'])
    label3.config(text=f"{data['main']['temp']} \u00B0C")  # \u00B0 is the degree symbol
    label4.config(text=f"Feels like {data['main']['feels_like']} \u00B0C")
    utc_time = datetime.utcfromtimestamp(data['dt'])

    local_time = utc_time + timedelta(seconds=data['timezone'])

    formatted_time = local_time.strftime("%H:%M")
    label2.config(text=f"{formatted_time} AM")
    
    #    print(data)
    # if data["success"] and "data" in data:
    # else:
    #     raise Exception("Failed to fetch User Data")
    
root=Tk()
root.geometry("1000x600")
root.configure(background='white')
root.title("My Weather App")

entry=Entry(root,background="#2c2d2d",width=30,font="Ariel 26",fg="white")
entry.place(x=20,y=20)
img = Image.open("assests/search.jpg")
img = img.resize((30, 36))
photo=ImageTk.PhotoImage(img)

   # Create a Label to display the image
def place_image():
        image_label = Button(root, image=photo, bg="#2c2d2d",command=fetch_random_quotes_freeapi)  # Match the Entry background color
        image_label.place(x=entry.winfo_x() + entry.winfo_width()-20 , y=20)  # Position it to the right of the Entry
        image_label.bind( "<Enter>", lambda e: image_label.config(cursor="hand2"))
        image_label.bind( "<Leave>", lambda e: image_label.config(cursor=""))

    # Use after to place the image after the main loop starts
root.after(10, place_image)






# middle

label=Label(root,text="Current Weather",font="comicsans 27 bold")
label.place(x=35,y=89)
label2=Label(root,text="03:27 AM",font="comicsans 27 bold")
label2.place(x=35,y=140)

img1=Image.open("assests/logo.png")
photo1=ImageTk.PhotoImage(img1)
image_label1=Label(root,image=photo1,bg='white')
image_label1.place(x=340,y=90)

label3=Label(root,text=f"0 \u00B0",font="comicsans 55 bold",background='white')
label3.place(x=600,y=150)
label4=Label(root,text=f"Clouds | FEELS LIKE 0 \u00B0",font="comicsans 18",background='white')
label4.place(x=600,y=240)

# bottom
f1=Frame(root,background="#3cdfff",width=40)
f1.pack(side='bottom')
labels = ["Wind", "Humidity", "Description", "Pressure"]
for i, text in enumerate(labels):
    l = Label(f1, text=text, background="#3cdfff", fg='white',font="comicsans 20 bold")
    l.grid(row=0, column=i, padx=50, pady=8)

wind_label = Label(f1, text="0 m/s", background="#3cdfff", fg='black',font="comicsans 20 bold")
wind_label.grid(row=1, column=0)

humidity_label = Label(f1, text="0%", background="#3cdfff", fg='black',font="comicsans 20 bold")
humidity_label.grid(row=1, column=1)

description_label = Label(f1, text="N/A", background="#3cdfff", fg='black',font="comicsans 20 bold")
description_label.grid(row=1, column=2)

pressure_label = Label(f1, text="N/A", background="#3cdfff", fg='black',font="comicsans 20 bold")
pressure_label.grid(row=1, column=3)
root.mainloop()