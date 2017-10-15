import threading
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

def function(i):
	print ("function called by thread %i\n" %i)
	return

thread = []
for i in range (5):
	t = threading.Thread(target=function, args=(i,))
	thread.append(t)
	t.start()
	t.join()