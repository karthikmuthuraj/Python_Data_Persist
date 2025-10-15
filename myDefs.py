# < reference > python_DATA_persistance_tutorial.pdf
# < purpose > routine for collating Functions in one file
import sys

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

