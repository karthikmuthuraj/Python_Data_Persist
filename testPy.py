# < reference > python_DATA_persistance_tutorial.pdf
# < purpose > Driver ROUTINE.

import myDefs
import time
import sys
import os

# conditions to excute code blocks
print(" Type CSV to execute CSV Module \n" \
      " Type RWL to execute Read Write \n" \
      " Type JSN to execute Json Module")

module = input("Enter the text: ")

print("IN:")
print("---")

if (module == "RWL"):
    # test1 = myDefs.readLine()
    intime0 = time.time()
    test0 = myDefs.readandwriteFile()
    outtime0 = time.time()

    intime1 = time.time()
    test1 = myDefs.readandwriteFile()
    outtime1 = time.time()

elif (module == "CSV"):
    test3 = myDefs.writeCSV()
    # test4 = myDefs.readCSV()

elif (module == "JSN"):
    print("JSON module to be written")

else:
    print("Please Type the relevant keyword")


print("OUT:")
print("----")

if (module == "RWL"):
    # print(test1)
    if (test0 == "SUCCESS"):
        print ("SIMPLE:TIME - file Read-Write : ",outtime0-intime0)

    if (test1 == "SUCCESS"):
        print ("OS:TIME - file Read-Write : ",outtime1-intime1)

    # update user based on the quickest time.
    if ((outtime0-intime0) < (outtime1-intime1) ):
        print ("SIMPLE time function is faster ")
    else:
        print ("OS time function is faster")

elif (module == "CSV"):
    if (test3 == "SUCCESS"):
        print ("CSVWRITE: SUCCESS")

    # if (test4 == "SUCCESS"):
    #    print ("CSVREAD: SUCCESS")  
    