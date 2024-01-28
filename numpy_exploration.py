import numpy as np
import time
import sys

l = range(1000)
print(sys.getsizeof(1)*len(l))

array = np.arange(1000)
print(array.size*array.itemsize)

SIZE = 1000000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.array(SIZE)
a2 = np.array(SIZE)

# python list
start = time.time()
result = [x+y for x,y in zip(l1,l2)]
print("Python list took : " ,(time.time()-start)*1000)

# np array
start = time.time()
result = a1+a2
print("numpy took : ", (time.time()-start)*1000)