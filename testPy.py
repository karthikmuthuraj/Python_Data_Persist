# execution routine.
from array import *

print("ARRAYs")
print('------')
# basic operations of an array
# Traverse / insertion / deletion / search / update

array2= array('i', [10,20,30])      # define an array
print(array2)                       # diplay the array
print(array2.index(30))             # displays the index of the value asked.

array2[2]=40                        # update the 2nd variable with value 40.
for x in array2:                    # loop to display the array
    print(x)