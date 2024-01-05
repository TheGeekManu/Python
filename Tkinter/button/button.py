from tkinter import *

#override legacy with themed widgets
from tkinter.ttk import *

#create new window
window = Tk()

#assign window title.
window.title('Button')

#create hello button
helloButton = Button(text="Click me")
helloButton.pack()


#run program
window.mainloop()