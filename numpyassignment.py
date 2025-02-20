import numpy as np
import time
def flat_method(arr):
    s=0
    start=time.time()
    for i in (arr).flat:
        s+=i
    end=time.time()
    t=end-start
    print(f'Sum:{s},TimeTaken:{t} of flatmethod')
def iter_method(arr):
    m=0
    start=time.time()
    for i in np.nditer(arr):
        m+=i
    end=time.time()
    t=end-start
    print(f'Sum:{m},TimeTaken:{t} of itermethod')
def random_numgen(l,h,s):
    arr=np.random.randint(l,h,s)
    return arr
arr=random_numgen(1,100,(2000,5000))
flat_method(arr)
iter_method(arr)
print(np.sum(arr))

