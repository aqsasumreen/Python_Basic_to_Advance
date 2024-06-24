# def function_1(name , age , number , city):
#     print("the name of Student" ,name ,"age is" , age , "Roll Number is " , number  , "city is" , city)
#
# function_1("Aqsa" , 20 , 21 , "sgd")

# ---------*ARGS-----------

def function_1(*vars):
    print(type(vars))
    print("the name of Student",vars[0],"age is",vars[1], "Roll Number is",vars[2])

# function_1("Aqsa",20 ,21 ,"sgd")
# Another way to pass List  is :
lis =["Azka" , "Sana" , 20]
function_1(*lis)

# ---------------**kwargs---------------

# def function_2(**vars):
#     print(type(vars))
#     for key , value in vars.items():
#             print(key , value)


# markList ={"aqsa" :20 , "Ali":21  ,"Omer" : 21}
# function_2(**markList)
# we can`t pass dictionary here in the way we passed vars in the function_1

#-----> Master function use both args and kwargs

# def master(normal , *args , **kwargs):
#     print(normal)
#     for i in args:
#         print(i)
#     for key ,value in kwargs.items():
#         print(key , value)
#
# lis =["Azka" , "Sana" , 20]
# markList ={"aqsa" :20 , "Ali":21  ,"Omer" : 21}
# master("its normal" , *lis , **markList)

