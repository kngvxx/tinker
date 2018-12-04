from task import *
window = Tk()

entry = Entry(window, text="")
entry.pack(side="bottom", fill="x")

addTaskBtn = Button(window, text="dodaj zadanie", command=lambda:PrepareTask(window, entry))
addTaskBtn.pack(side="bottom", fill="x")

# AddRowForTask(window, "1", "buton")
# AddRowForTask(window, "2", "inna nazwa")
window.mainloop()

