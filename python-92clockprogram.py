try:
    import Tkinter as tk
except:
    import tkinter as tk
from tkinter import *
import time


def update():
    time_string = time.strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = time.strftime("%A")
    day_label.config(text=day_string)

    date_string = time.strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)
window = Tk()


time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="Black")
time_label.pack()

day_label = Label(window,font=("Arial",25),fg="#00FF00",bg="Black")
day_label.pack()

date_label = Label(window,font=("Arial",30),fg="#00FF00",bg="Black")
date_label.pack()

update()




# window.configure(bg='red')
window['bg'] = 'black'


window.mainloop()