from tkinter import Entry

import tkinter

window = tkinter.Tk()

window.title("Miles to KM converter")
window.minsize(width=400, height=300)
window.config(padx=100, pady=100)


km = Entry(window)
km.grid(column=2, row=1)


l1 = tkinter.Label(window, text="Miles")
l1.grid(column=3, row=1)

l2 = tkinter.Label(window, text="is equal to")
l2.grid(column=1, row=2)

l3 = tkinter.Label(window, text="0")
l3.grid(column=2, row=2)

def milestokm():
    miles = float(km.get())
    kilometers = miles * 1.609
    l3.config(text=f"{kilometers}")



l4 = tkinter.Label(window, text="KM")
l4.grid(column=3, row=2)

cal = tkinter.Button(window, text="Calculate")
cal.config(command=milestokm)
cal.grid(column=2, row=3)

window.mainloop()
