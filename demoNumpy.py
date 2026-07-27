import numpy as np
import time

def timer(func):
    def warpper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        cost = (time.time() - start) * 1000
        print(f"函数 {func.__name__} 耗时：{cost:.4f} ms")
        return ret
    return warpper

@timer
def list_square(lst):
    return [x ** 2 for x in lst]

@timer
def ndarray_square(arr):
    return arr ** 2

data = list(range(10**6))
print(type(data))
arr = np.array(data)
print(type(arr))

#计算结果比对两者性能差异
list_square(data)
ndarray_square(arr)

