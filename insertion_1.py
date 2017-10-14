import time
from random import randint
# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

   # Traverse through 1 to len(arr)
   for i in range(1, len(arr)):

       key = arr[i]

       # Move elements of arr[0..i-1], that are
       # greater than key, to one position ahead
       # of their current position
       j = i-1
       while j >=0 and key < arr[j] :
               arr[j+1] = arr[j]
               j -= 1
       arr[j+1] = key


# Driver code to test above

l = randint(3*10**4,3*10**5)
arr = []
for i in range(l):
 arr.append(randint(3*10**4,3*10**5))
start_time = time.time()
insertionSort(arr)
print ("Sorted array is:", arr)
exec_time = (time.time() - start_time)
print("\nExecution time: %s seconds" % exec_time)