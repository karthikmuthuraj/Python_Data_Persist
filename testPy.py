# < reference > python_DATA_persistance_tutorial.pdf
# < purpose > Driver ROUTINE.

import myDefs
import time
import sys
import os

'''
print(f"Script Name: ")
'''
print(f"Script Name: ")
# conditions to excute code blocks
print("Type CSV to Call CSV Module \n" \
      "Type RWL to Call Read Write \n" \
      "Type JSN to Call Json Module \n")

module = input("Enter the Module Keyword: \t")
'''

'''


if ({sys.argv[1]}[3:0]== "RWL"):
    
    # print("IN:")
    # print("---")
    
    
    # print("IN:")
    # print("---")
    
    # test1 = myDefs.readLine()
    
    
    intime0 = time.time()
    test0 = myDefs.readandwriteFile()
    outtime0 = time.time()

    intime1 = time.time()
    test1 = myDefs.readandwriteFile()
    outtime1 = time.time()

elif ({sys.argv[1]}[3:0] == "CSV"):
    test3 = myDefs.writeCSV()
    # test4 = myDefs.readCSV()

elif ({sys.argv[1]}[3:0] == "JSN"):
    print("\nJSON module to be written")

else:
    print("\nCode EXIT : TYPE in the CORRECT keyword\n")
    exit(0)

if ({sys.argv[1]}[3:0] == "RWL"):

    print("OUT:")
    print("----")

    print("OUT:")
    print("----")
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

elif ({sys.argv[1]}[3:0] == "CSV"):
    if (test3 == "SUCCESS"):
        print ("CSVWRITE: SUCCESS")

    # if (test4 == "SUCCESS"):
    #    print ("CSVREAD: SUCCESS")  

elif ({sys.argv[1]}[3:0] == "JSN"):
    print("JSON module WRITTEN")

else:
    print("\nNo Specific Module Initiated")
    exit(0)