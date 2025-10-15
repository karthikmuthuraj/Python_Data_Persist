# < reference > python_DATA_persistance_tutorial.pdf
# < purpose > routine for collating Functions in one file
import sys
import os

def readLine():
    print("Enter the text: ")
    return sys.stdin.readline()

def readandwriteFile():
    with open("IN\\file_inp.txt", "r+") as f:   # r+ amd w+ facilitates read and write operations when files are open
        content = f.readlines()                 #   so, no need to close the file before opening another file in parallel
        g = open("OUT\\file_out.txt", "w+")     
        g.writelines(content)
    g.close()

    return "SUCCESS"

def readandwriteFile_OS():
    f =os.open("IN\\file_inp.txt", os.O_RDONLY)
    content = os.read(f,100)                 
    os.close(f)
    
    g = os.open("OUT\\file_out.txt", os.O_WRONLY | os.O_CREAT)     
    os.write(g,content)
    os.close(g)

    return "SUCCESS"

