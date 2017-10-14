def radixSort(a,n,maxLen):
    for x in range(maxLen):
        bins = [[] for i in range(n)]
        for y in a:
            bins[(y/n**x)%n].append(y)
        a=[]
        for section in bins:
            a.extend(section)
    return a

if __name__ == "__main__":
    import random
    import timeit
    a = []
    for i in range(0, 100000):
		a.append(random.randint(1, 1500))
    t = timeit.Timer('radixSort(a, 10, 5)', 'from __main__ import radixSort, a')
    print t.timeit(number=1)