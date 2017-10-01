'''
Write a program that creates ten threads that shows its thread 
number and prints "Hello!" three times.  
The thread should print "Bye!" before exiting.
'''

import threading
import time

exitFlag=0

class myThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter=counter
	def run(self):
		print ("Starting "+self.name)
		print_hello(self.name, self.threadID, self.counter, 3)
		print ("\n")
		print ("[Bye! "+self.name+"]")

def print_hello(threadName, threadID, delay, counter):
	while counter:
		if exitFlag:
			thread.exit()
		time.sleep(delay)
		print ("%s Hello World" %threadID)
		counter -=1

#Create new Threads

thread1=myThread(1, "Thread-1", 3)
thread2=myThread(2, "Thread-2", 3)
thread3=myThread(3, "Thread-3", 3)
# thread4=myThread(4, "Thread-4", 3)
# thread5=myThread(5, "Thread-5", 3)
# thread6=myThread(6, "Thread-6", 3)
# thread7=myThread(7, "Thread-7", 3)
# thread8=myThread(8, "Thread-8", 3)
# thread9=myThread(9, "Thread-9", 3)
# thread10=myThread(10, "Thread-10", 3)

#Start new Threads
thread1.start()
thread2.start()
thread3.start()
# thread4.start()
# thread5.start()
# thread6.start()
# thread7.start()
# thread8.start()
# thread9.start()
# thread10.start()

print ("Exiting Main Thread") 
