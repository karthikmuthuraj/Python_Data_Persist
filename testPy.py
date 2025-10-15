# < reference > python_DATA_persistance_tutorial.pdf
# < purpose > Driver ROUTINE.

import myDefs
import time

print("IN:")
print("---")

# test1 = myDefs.readLine()
intime = time.time()
test2 = myDefs.readandwriteFile()
outtime = time.time()

print("OUT:")
print("----")

print(intime)
print(outtime)
# print(test1)
if (test2 == "SUCCESS"):
    print ("TIME - file Read-Write : \n", outtime-intime)