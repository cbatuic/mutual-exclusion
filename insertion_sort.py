import time
from random import randint

# Serial Version for Insertion Sort
def insertion_sort(list):
	iteration = 0
	for index in range(1,len(list)):
		iteration += 1
		print("iteration", iteration)
		value = list[index]
		i = index - 1
		while i>=0:
			print(">>>", lst)
			if value < list[i]:
				list[i+1] = list[i]	#shift number in slot i right to slot i+1
				list[i] = value 	#shift value left into slot i
				i = i - 1
			else:
				break				

# Main Method
snum = 1	# starting random number
enum = 10	# ending random number
tnum = 100	# total number of elements in the list
lst = []
for i in range(tnum):
	lst.append(randint(snum,enum))
start_time = time.time()	
insertion_sort(lst)
print("\nresult:",lst)
exec_time = (time.time() - start_time)
print("Execution time: %s seconds" % exec_time)