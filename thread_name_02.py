import threading
import time

def function():
	print (threading.currentThread().getName() + str(' is Starting \n'))
	time.sleep(2)
	print (threading.currentThread().getName()+str(' is Exiting \n'))
	return

if __name__=="__main__":
	t1 = threading.Thread (name='first_function', target=function)
	t2 = threading.Thread (name='second_function', target=function)
	t3 = threading.Thread (target=function)

	t1.start()
	t2.start()
	t3.start()
	t1.join()
	t2.join()
	t3.join()