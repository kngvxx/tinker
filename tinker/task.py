from tkinter import *
lineCount = 1

def AddRowForTask(window, text, name):
    frame = Frame(window)
    frame.pack()
    checkbox = Checkbutton(frame, name=name+"cbx")
    checkbox.pack(side="left")
    label = Label(frame, text=text)
    label.pack(side="left")
    editbtn = Button(frame, text="edytuj", name=name+"editbtn", command=lambda:Run(name+"editbtn"))
    editbtn.pack(side="left")
    deletebtn = Button(frame, text="usuń", name=name+"deletebtn", command=lambda:Run(name+"detelebtn"))
    deletebtn.pack(side="left")


def PrepareTask(window, entry):
    global lineCount
    AddRowForTask(window, entry.get(), str(lineCount))
    lineCount += 1


def Run(name):
    print(name)