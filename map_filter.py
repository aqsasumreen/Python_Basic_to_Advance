# map=(Function to Apply , List of Inputs)
lis1 = [4, 7, 8, 2]
sq = []
for i in lis1:
    sq.append(i**2)
print(sq)

#---> Another way
def square(n):
    return n**2
sq= list(map(square , lis1))
print(sq)

list_1 = [2, 3, 3]
def double_num(numbers):
    return numbers*2
print(list(map(double_num , list_1)))
print(list(map(lambda num : num**2, list_1)))


# ----------------->Filter funct: it will return list for True
def greater_than_2(n):
    if n>2:
        return True
    else:
        return False
h1 = [3, 6, 7 ,1, -2, -5]
fil = list(filter(greater_than_2 , h1))
print(fil)
h3 = [3, 4, 9, 8, 6]
print(list(filter(lambda h3: h3 % 2 == 0, h3)))

# --> Reduce Function

from functools import reduce
def sub(a,b):
    return a-b

print(reduce(sum , [10,6,3]))
