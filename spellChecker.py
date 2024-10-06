from spellchecker import SpellChecker
from tkinter import *

root=Tk()
root.geometry("1000x600")
root.configure(background='#Add8e6')

def correct_text():
    text=entry.get("1.0", "end-1c")
    if text !='':
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = spell.correction(word)
            if corrected_word != word.lower():
                print(f'Correcting "{word}" to "{corrected_word}" ')
                corrected_words.append(corrected_word)

        corrected_text= ' '.join(corrected_words)
        label.config(text=f'Corrected Spelling is: {corrected_text}')
        

Label(root,text="Spell Checker",font="comicsansms 30 bold",background="#Add8e6").place(relx=0.5,rely=0.2,anchor=CENTER)

entry=Text(root,background='#fff',width=40,height=1,font="Ariel 20",fg="black")
entry.place(relx=0.5,y=200,anchor=CENTER)

button=Button(root,background='red',foreground='white',width=12,height=1,text="Check",command=correct_text)
button.bind( "<Enter>", lambda e: button.config(cursor="hand2"))
button.bind( "<Leave>", lambda e: button.config(cursor=""))
button.place(relx=0.5,y=260,anchor=CENTER)

label=Label(root,text='',font='comicsans 20',background='#Add8e6')
label.place(relx=0.3,y=300,anchor=CENTER)


spell = SpellChecker()



    


root.mainloop()
