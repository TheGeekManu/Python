from tkinter import *

#override legacy with themed widgets
from tkinter.ttk import *

#create new window
window = Tk()

#assign window title.
window.title('Input')

def buttonClicked():
    name = 'Your name is ' + str(nameEntry.get())
    displayLabel.configure(text=name)
    nameEntry.config(text="")

#create label
nameLabel = Label(text='Enter your name')
nameLabel.pack()

#create entry
nameEntry = Entry()
nameEntry.pack()

#create button
enterButton = Button(text='Enter name', command=buttonClicked)
enterButton.pack()

#create display label
displayLabel = Label()
displayLabel.pack()



#run program
window.mainloop()