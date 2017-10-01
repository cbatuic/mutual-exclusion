'''
Author: 
Clyde Balaman

Problem: 
Thread Locking Exercise

Description:
Write a program that creates a list of random numbers.  
The random numbers in the list can be from numbers 1 to 10.  
There should be 200 elements in the list. 

After creating the list, the program should use at least two 
threads the would count the frequency of a given number.  
The number to be counted should be an input from the user.

Example interaction / output:

Enter the number to be counted (1-10):  5
Creating list....
Counting the frequency of number 5
The number 5 has a count of 30
'''

import logging
from random import randint
import threading
import time


# >>>>>>>> User Input
number_tobe_counted = int(input("Enter number to be counted(1-10): "))
# print(number_tobe_counted)

print ("Creating list....")


# >>>>>>>> List Creation
start_number = 1
end_number = 10
total_elements = 5
list_random_numbers = []
for i in range(total_elements):
       list_random_numbers.append(randint(start_number,end_number))
# print('Randomised list is: ',list_random_numbers)


print('Randomised list is: ',list_random_numbers)
print ("#######################################")

print ("Counting the frequency of number {}".format(number_tobe_counted))
total_frequency_count = 0



logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
                    
class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start
    def increment(self):
        # logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            # logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()

def worker(c):

	if c.value <= total_elements-2:
	    for i in range(total_elements-2):
	        pause = 1
	        # logging.debug('Sleeping %0.02f', pause)
	        time.sleep(pause)
	        
	        curr_element = list_random_numbers[c.value]
	        # logging.debug("CE:{} NTC:{}".format(curr_element,number_tobe_counted))
	        global total_frequency_count
	        if curr_element == number_tobe_counted:
	            total_frequency_count +=1
	            # logging.debug("counter incremented: %d", c.value)
	        c.increment()

    # logging.debug('Done')

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

# logging.debug('Waiting for worker threads')
main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
# logging.debug('Counter: %d', counter.value)
logging.debug("The number {} has a count of {}".format(number_tobe_counted, total_frequency_count))
