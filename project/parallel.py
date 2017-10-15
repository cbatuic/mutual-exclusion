import threading

def function(i):
	print ("function called by thread %i" %i)
	insertion_sort()
	return

def insertion_sort():
	print("sorting...")
	print("\n")

if __name__=="__main__":
	thread = []
	for i in range (2):
		t = threading.Thread(target=function, args=(i,))
		thread.append(t)
		t.start()
		t.join()