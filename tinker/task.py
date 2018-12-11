from tkinter import *
lineCount = 1

archivedTasks = []

def AddRowForTask(window, text, name):
    frame = Frame(window, name=name)
    frame.pack()
    checkbox = Checkbutton(frame, name=name+"cbx", command=lambda: FinishTask(window, frame, text))
    checkbox.pack(side="left")
    label = Label(frame, text=text, height=2)
    label.config(font=("Times New Roman", 12))
    label.pack(side="left")
    editbtn = Button(frame, text="edytuj", name=name+"editbtn", command=lambda: Run(name+"editbtn"))
    editbtn.pack(side="left")
    deletebtn = Button(frame, text="usuń", name=name+"deletebtn", command=lambda: Run(name+"detelebtn"))
    deletebtn.pack(side="left")


def FinishTask(window, frame, text):
    global archivedTasks
    archivedTasks.append(text)
    print(archivedTasks)
    frame.pack_forget()
    frame.destroy()
    window.update()


def PrepareTask(window, entry):
    global lineCount
    AddRowForTask(window, entry.get(), str(lineCount))
    lineCount += 1
    window.update()


def Run(name):
    print(name)