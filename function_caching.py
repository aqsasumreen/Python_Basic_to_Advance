# When a function runs again and again for the same value
# Memoize = to save the result of a calculation so you can use it
# later without doing the calculation again

# Function caching is technique  for improving the performance of  program  by storing
# the results of function call ,so you can use the results instead of recomputing them
# every time function called , useful when function is computationally expensive.

from functools import lru_cache
import time


@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n * 3


print(fx(4))
print("done for 4")
print(fx(5))
print("done for 5")
print(fx(4))  # dobara compute nhi kry ga cache se hi uthaye ga
print("done for 4")  # cache aik hi run me hti, dobara krny se khtm ho jati
print(fx(5))
print("done for 5")
