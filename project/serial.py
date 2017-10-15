import time
from random import randint

def insertionSort(arr):
  global moves
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >=0 and key < arr[j] :
      moves += 1
      arr[j+1] = arr[j]
      j -= 1
      arr[j+1] = key

if __name__=="__main__":
  moves = 0
  l = randint(1000,10000)
  arr = []
  
  for i in range(l):
   arr.append(randint(3*10**4,3*10**5))
  
  start_time = time.time()
  insertionSort(arr)
  exec_time = (time.time() - start_time)
  
  print ("Sorted array is:", arr)
  print("\n")
  print("Total Elements: %s" % l)
  print("Moved Elements: %s" % moves)
  print("Execution time: %s seconds" % exec_time)

#$ py -2 serial.py