# iterable -- a Python object that uses __iter or __getitem functions, which give us an iterator.
# iterators -- an object with a next method that gives us the next element.
# iteration -- going through something and getting its next elements is called iteration.
# Generators -- special Python functions that create an iterable sequence of values.
# They return a generator object that can generate values one by one when we iterate over it.
# Generators are useful for working with large and complex sets because they create values on the fly.
# We create generators using the yield keyword.
# The next function is used to get the next value.

def generator(n):
    for i in range(n):
        yield i


#---> way#1

gen = generator(100)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

#----> way#2

for i in gen:
    print(i)

num = 344
# INT OBJECTS ARE NOT ITERABLE...
# for i in num:  # error occured
#     print(i)

# var = "aqsa"
# iter1 = iter(var)
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
