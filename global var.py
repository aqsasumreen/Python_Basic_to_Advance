l=10
def fun1(n):
    #l=3
    m=9
    #changing the value of global var
    global l
    l=l+5
    print(l,m)
    print(n,"i have done")


fun1("this is me")
print(l)

def harry():
    x=20
    #print(n , "aqsa")
    def rohan():
        global x
        x=88
        print("before calling rohan:" , x)
        rohan()
        print("after calling rohan:", x)

harry()

# ===================> How to chg Global Variables <========================
x = 10


def function_a():
    global x
    x = 5
    y = 6
    print(y)


function_a()
print(x)
