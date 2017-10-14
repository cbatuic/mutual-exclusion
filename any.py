import threading
import sys
import timeit
from random import randint

threadCount = 0
#list = [50, 34, 22, 565, 3, 55, 1045, 3333, 344, 988, 51, 13, 20, 17, 77, 18, 5, 8, 9, 4, 106, 333, 5534, 3424, 1534, 434, 401, 23, 55]
list = []

class Sorter(threading.Thread):
    def __init__(self, mode):
        global threadCount
        threading.Thread.__init__(self)
        self.mode = mode
        self.lock = threading.Lock()
        self.list = []
        threadCount = threadCount + 1
    def run(self):
        global list
        passes = 0
        for i in range(0, len(list)):
            if (self.mode  == "one"):
                if (list[i] >= 0 and list[i] <= 9):
                    self.list.append(list[i])
            elif(self.mode == "tens"):
                if (list[i] >= 10 and list[i] <= 99):
                    self.list.append(list[i])
            elif(self.mode == "hundreds"):
                if (list[i] >= 100 and list[i] <= 999):
                    self.list.append(list[i])
            elif(self.mode == "thousands"):
                if (list[i] >= 1000 and list[i] <= 9999):
                    self.list.append(list[i])
        bucket = [[], [], [], [], [], [], [], [], [], []]
        if   (self.mode == "one"):
            passes = 1
        elif (self.mode == "tens"):
            passes = 2
        elif (self.mode == "hundreds"):
            passes = 3
        elif (self.mode == "thousands"):
            passes = 4

        for i in range(0, passes):
            nlist = []
            for j in range(0, len(self.list)):
                curr = str(self.list[j])
                bucket[int(curr[passes - i - 1])].append(self.list[j])

            for j in range(0, 10):
                for k in range(0, len(bucket[j])):
                    nlist.append(bucket[j][k])
            self.list = nlist
            bucket = [[], [], [], [], [], [], [], [], [], []]

class Merger():
	@staticmethod
	def join(*args):
		res = []
		for i in range(0, len(args)):
			res += args[i]
		return res

def sort(l):
	t1 = Sorter("one")
	t2 = Sorter("tens")
	t3 = Sorter("hundreds")
	t4 = Sorter("thousands")
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t1.join()
	t2.join()
	t3.join()
	t4.join()
	#print(Merger.join(t1.list, t2.list, t3.list, t4.list))

if __name__=="__main__":
	for i in range(0, 100000):
		list.append(randint(1, 1500))
	t = timeit.Timer('sort(list)', 'from __main__ import sort, list')
	print t.timeit(number=1)
	