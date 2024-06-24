add = lambda x, y: x + y
print(add(5, 8))

a = [(2, 5), (1, 9), (5, 4)]
a.sort(key=lambda x: x[0])
print(a)


# It will sort based on the value at index 0, and x[1] will sort based on the second element.
# lambda functions are used to pass as an argument to the other function

def apply(fx, value):
    return 5 + fx(value)


print(apply(lambda x: x * 2, 2))
