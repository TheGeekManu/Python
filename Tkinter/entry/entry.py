from tkinter import *

#override legacy with themed widgets
from tkinter.ttk import *

#create new window
window = Tk()

#assign window title.
window.title('Entry')

#create new entry window
randomEntry = Entry(width=30)
randomEntry.pack()

#run program
window.mainloop()