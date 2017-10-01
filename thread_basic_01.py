import threading

def function(i):
	print ("function called by thread %i\n" %i)
	return

thread = []
for i in range (5):
	t = threading.Thread(target=function, args=(i,))
	thread.append(t)
	t.start()
	t.join()