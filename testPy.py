# < reference > python_DATA_persistance_tutorial.pdf
# < purpose > Driver ROUTINE.

import myDefs
import time

print("IN:")
print("---")

'''

# test1 = myDefs.readLine()
intime0 = time.time()
test0 = myDefs.readandwriteFile()
outtime0 = time.time()

intime1 = time.time()
test1 = myDefs.readandwriteFile()
outtime1 = time.time()



test3 = myDefs.writeCSV()
'''
test4 = myDefs.readCSV()


print("OUT:")
print("----")

'''

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

if (test3 == "SUCCESS"):
    print ("CSVWRITE: SUCCESS")

'''
if (test4 == "SUCCESS"):
    print ("CSVREAD: SUCCESS")  
    