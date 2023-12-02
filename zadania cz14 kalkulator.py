from tkinter import *
import math

def square():
    res1 = math.sqrt(int(entry1.get()))
    mytext.set(res1)

ws = Tk()
ws.title("Python zadania")
ws.geometry("500x300")
mytext = StringVar()
Label(ws, text="Number").grid(row=0, sticky=W)
Label(ws, text="Result:").grid(row=2, sticky=W)
result = Label(ws, text="", textvariable = mytext).grid(row=2, column=1, sticky=W)

entry1 = Entry(ws)

entry1.grid(row=0, column=1)

button = Button(ws, text="Calculate", command=square)
button.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)

ws.mainloop()