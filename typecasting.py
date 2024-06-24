
# ************* Explicit typecasting
a = 4
b = 6
print(str(a) + str(b))

# ************* Implicite typecasting

# Some data types have low order some has high order so implicite convrt lower to higher
c = 3
d = 5.5
print(c + d ) #Answer in in highr order which is float

# Input function takes a string only so, for other types we used typecasting
e = input("Enter a number: ")
f = input("Enter a number: ")
print(int(e) + int(f))