import myDefs

# Python program to create 
# a file explorer in Tkinter
  
# import all components
# from the tkinter library
from tkinter import *

# Create the root window
window = Tk()
  
# Set window title
window.title('Robocopy')
  
# Set window size
window.geometry("200x200")
  
#Set window background color
window.config(background = "white")

  
# Create a File Explorer label
label_file_explorer = Label(window, 
                            text = "File Explorer - Tkinter",
                            width = 20, height = 2, 
                            fg = "blue")
  
      
button_sourcefold = Button(window, 
                        text = "Source Folder",
                        command = myDefs.browseFolderPath) 

button_destfold = Button(window, 
                        text = "Dest Folder",
                        command = myDefs.browseFolderPath) 

button_launchshell = Button(window,
                        text = " Robocopy",
                        command = myDefs.launchshell)  

button_exit = Button(window, 
                     text = "Exit",
                     command = exit) 
  
# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns
label_file_explorer.configure(text="File Opened:")
label_file_explorer.grid(column = 1, row = 1)
  
button_sourcefold.grid(column = 1, row = 2)
button_destfold.grid(column = 1, row = 3)
button_launchshell.grid(column = 1, row = 4)  
button_exit.grid(column = 1,row = 5)
  
# Let the window wait for any events
window.mainloop()