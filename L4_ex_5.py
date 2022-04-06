list = [r for r in range(100, 1000) if r % 128 == 0]
print(list)
from functools import reduce
def my_func(r_p, r):
    return r_p * r
print(reduce(my_func, list))
