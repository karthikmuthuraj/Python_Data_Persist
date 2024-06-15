import subprocess
# import filedialog module
from tkinter import filedialog

def launchshell():
    file1 = subprocess.run(["dir"])
    print("The exit code was: %d" % file1.returncode)

# Function for opening the 
# file explorer window
def browseFolderPath():
    """  TO launch explorer & READ files 
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    """
    # returns the folder name 
    foldername = filedialog.askdirectory(initialdir= "/")

    # Change label contents
    # label_file_explorer.configure(text="File Opened: "+ foldername)      