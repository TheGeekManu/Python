from tkinter import *

#override legacy with themed widgets
from tkinter.ttk import *

#create new window
window = Tk()

#assign window title.
window.title('Label')

#add a label.
helloLabel = Label(text="Hello World", 
#change foreground color
foreground='white',
#change background color 
background='red',
)

helloLabel.pack()

#run program
window.mainloop()