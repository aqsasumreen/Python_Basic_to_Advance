# ******************** Function
# def gemMean(a, b):
#      print("gemMean" , ((a+b)/(a*b)))
#
# gemMean(3,4)

# *************Types of Arguments ****************
# there is four types of arguments:-
# 1- default argument
# 2- Keyword arguments
# 3- Required arguments
# 4 - variable length arguments

# 1------- default argument
def avg(c=4, d=5):
    print("avg", (c + d) / 2)

# avg() #agr yha pr b value dety tou yhi execute ho gi

# 2------- Keyword arguments
def gemMean(a, b):
    print("gemMean", ((a + b) / (a * b)))

# gemMean(b=3, a=4)

# 3------- Required arguments
def sum(e, f):
    print("sum", e + f)

# sum(7,9) #if we pass only one then it causes problem

# 4 ------- variable length arguments

def average(*num):
    sum = 0
    for i in num:
        sum += i
    # print("average",sum/len(num))

# average(3,4,5,6,7) # passed list

def name(**names):  # passed dictionary
    print(type(names))
    print("Name", names["fname"], names["lname"])


# name(fname = "Aqsa" , lname = "Sumreen" )

#-------built in functions

list= [3 ,0 ,6 , 9]
print(abs(-4))
print(all(list)) #return if all true
print(any(list)) #return any is true
print(len(list))
print(min(list))
print(max(list))
print(sum(list))
print(type(list))
