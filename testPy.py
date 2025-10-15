# < reference > python_DATA_persistance_tutorial.pdf
# < purpose > Driver ROUTINE.

import myDefs

print("IN:")
print("---")

# test1 = myDefs.readLine()
test2 = myDefs.readandwriteFile()

print("OUT:")
print("----")

# print(test1)
if (test2 == "SUCCESS"):
    print ("file Read-Write SuCCESS \n")