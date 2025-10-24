# < reference > python_DATA_persistance_tutorial.pdf
# < purpose > routine for collating Functions in one file

import csv
import sys
import os

# declarations in general
persons = [ ('John', 'Doe', 28),
            ('Jane', 'Smith', 34),  
            ('Emily', 'Jones', 22) ]

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

def writeCSV():
    # define an output CSV file to store results.
    with open('OUT\\CSV_Outfile.csv', mode='w+', newline='') as file:
        writer = csv.writer(file)
        for person in persons:
            writer.writerow(person)

    file.close()

    return "SUCCESS"

def readCSV():
    with open('OUT\\CSV_Outfile.csv', mode='r+') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    file.close()

    return "SUCCESS"
