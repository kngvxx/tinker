from tkinter import *

window = Tk()
window.configure(background='black')
linia=0
def AddRowForTask(text, name):
    frame = Frame(window)
    frame.pack()
    checkbox = Checkbutton(frame, name=name+"chx")
    checkbox.pack(side="left")
    label = Label(frame, text=text)
    label.pack(side="left")
    editbtn = Button(frame, text="edit", name=name+"editbtn", command=lambda:Run(name+"editbtn"))
    editbtn.pack(side="left")
    deletebtn = Button(frame, text="delete", name=name+"deletebtn", command=lambda:Run(name+"deletebtn"))
    deletebtn.pack(side="left")

labelka = Entry(window, text="")
labelka.pack(side="bottom")

def Preparetask():
    global linia
    AddRowForTask(labelka.get(), str(linia))
    linia+=1

addTaskBtn = Button(window, text="Add Task", command=Preparetask)
addTaskBtn.pack(side="bottom", fill="x")





def Run(name):
    print(name)


AddRowForTask("1","baton")
AddRowForTask("1","inna nazwa")
window.mainloop()
