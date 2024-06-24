n=5
for i in range(n):
    for j in range(n):
        print("*" , end=  "   ")
    print()
n=5
for i in range(n):
    for j in range(i+1): #star on row is equal to line no +1
        print("*" , end="")
    print()
n=5
for i in range(n):
    for j in range(n-i):
        print("*" , end=  "   ")
    print()

#right side triangle

n=5
for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
    print()

#right sided triangle

n=5
for i in range(n):
    for j in range(i+1):
        print(" ", end="")
    for k in range(n-i):
        print("*", end="")
    print()

# upper hill part

n=5
for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i+1):
        print("*", end=" ")#>>increase space
    print()

#lower hill part

n=5
for i in range(n):
    for j in range(i+1):
        print( " " , end="")#>>readuce space
    for k in range(n-i):
        print("*", end=" ")
    print()

 #diamond
n=5
for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i+1):
        print("*", end=" ")#>>increase space
    print()

n=5
for i in range(n):
    for j in range(i+1):
        print( " " , end="")#>>reduce space
    for k in range(n-i):
        print("*", end=" ")
    print()

#table
n=2
for i in range(2 ,4):
    for j in range(1,11):
        print(i, "X" , j ,"=" ,i*j)
    print()