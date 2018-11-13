from tkinter import *
window=Tk()
label=Label(window, text="napis")
def hello():
    label['text']='inny'

    btn=Button(window,text="guzik",command=hello)

    btn.pack()
    label.pack()

    window.mainloop()