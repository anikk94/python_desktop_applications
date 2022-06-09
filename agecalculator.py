from calendar import month
import tkinter as tk
import datetime
from unicodedata import name
from PIL import Image, ImageTk

def getInput():
    name = nameEntry.get()
    year = yearEntry.get()
    month = monthEntry.get()
    date = dateEntry.get()
    full_date = datetime.date(int(year), int(month), int(date))
    person = Person(name, full_date)
    textArea = tk.Text(master=window, height=10, width=25)
    textArea.grid(column=1, row=6)
    answer = "Hi {person}. You are {age} years old.".format(person=name, age=person.age())
    textArea.insert(tk.END, answer)

window = tk.Tk()
window.geometry("620x780")
window.title("age calculator app")


name = tk.Label(window, text="Name")
name.grid(column=0, row=1)
nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)
year = tk.Label(window, text="Year")
year.grid(column=0, row=2)
yearEntry = tk.Entry()
yearEntry.grid(column=1, row=2)
month = tk.Label(window, text="Month")
month.grid(column=0, row=3)
monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)
date = tk.Label(window, text="Date")
date.grid(column=0, row=4)
dateEntry = tk.Entry()
dateEntry.grid(column=1, row=4)

window.mainloop()
