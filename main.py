from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(celsius.get())
        farenheit.set(int((value * (9/5) + 32)))
    except ValueError:
        pass


root = Tk()
root.title('Temperature Converter')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)



celsius = StringVar()
celsius_entry = ttk.Entry(mainframe, textvariable=celsius, width=7)
celsius_entry.grid(column=2, row=1)

farenheit = StringVar()
farenheit_label = ttk.Label(mainframe, textvariable=farenheit, width=7)
farenheit_label.grid(column=2, row=2)

ttk.Label(mainframe, text="Enter temperature in celsius: ").grid(column=1, row=1, sticky=(W))

ttk.Label(mainframe, text="This is the temperature in farenheit: ").grid(column=1, row=2)

ttk.Button(mainframe, command=calculate, text="Calculate").grid(column=2, row=3)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

celsius_entry.focus()
farenheit_label.focus()
root.bind("<Return>", calculate)

root.mainloop()