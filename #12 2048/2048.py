import requests
import json
from tkinter import *

window = Tk()

window.title('Covid-19')
window.geometry('220x70')

lbl = Label(window,
            text = "Total archive case:-.....")
lbl1 = Label(window,
            text = "Total confirmed cases:-...")

lbl.grid(column=1, row=0)
lbl1.grid(column=1, row=1)
lbl2 = Label(window, text="")
lbl2.grid(column=1, row=3)

def clicked():
    url = "https://api.covid19india.org/v4/min/data-all.min.json"
    page = requests.get(url)
    data = json.load(page.text)

    lbl.configure(text = "Total active cases:-"
                + data["statewise"][0]["active"])

    lbl1.configure(text = "Total confirmed cases:-"
                + data["statewise"][0]["confirmed"])

    lbl2.configure(text="Data refreshed")

btn = Button(window, text="Refresh", command = clicked)
btn.grid(column=2, row=0)

window.mainloop()