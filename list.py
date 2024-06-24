#-----Lists are mutable------
my_list1 = [1 ,2 ,3 ,'ali' , 'Python']
print(my_list1)

#--------->Accessing list elements<----------

my_list2 = list([2 ,6 ,'AliS' , "sana" ,"saba"])
print(my_list2)
print(my_list2[2])
print(my_list2[0:2])
print(my_list2[: :-1])
print(my_list2[0:5:3])
print(my_list2[2][3])
print(my_list2[:3])

#-----> ADVANCE LISIT SLICING

lisit_1 =[2,4,5,6,7,8,9,3]
print(lisit_1[-5:-2])

# it will move forward

print(lisit_1[: : -1])
string_1 = "This is my book."
print(string_1[: :-1])
print(lisit_1[-2:])
print(lisit_1[:-2])
print(lisit_1[: : -2])

#-------> -ve slicing

list_1 = [2,4,6,8,10,12, 14]
print(list_1[-2::])

# TO REVERSE A LIST

print(list_1[::-1])
print(list_1[2:-2:])
print(list_1[-5:-2])

# ------>Test

list = [2,4,6,8,10,12, 14]
print(list[::2])
print(list[::])
print(list[2::])
print(list[2::2])

#---->Adding element to the list

my_list1=[1 ,2 ,3 , 3,"ALi" , "SANA"]
my_list2=[4 ,5,6 ,"aqsa" , "SAbA"]
'''my_list1.append([23 ,45])
print(my_list1)
print(len(my_list1))'''
my_list2.extend([23 ,45])
print(my_list2)
print(len(my_list2))
my_list2.insert(1 ,"Omer")
print(my_list2)
print(len(my_list2))
print(my_list1+ ['just exp'])
print(my_list1 * 2)
print(max(my_list1))

# ----------> list Methods ----------

my_list1.sort(reverse=True)
my_list1.reverse()
print(my_list1.count(3))
print(my_list1.index("ALi"))
m=my_list1.copy()
print(m)


#------->DELELTING ELEMENTS OF LIST

my_list3 =[4 ,5,6 ,"ali" , "python" , 10]

print( my_list3)
del my_list3[5]
print( my_list3)
my_list3.remove("python")
print( my_list3)
a=my_list3.pop(1)
print("poping alem is " , a , "remaining is" , my_list3)
my_list3.clear()
print(my_list3)

#--------->OTHER FUNCTIONS

print(len(my_list3))
print( my_list3.index("python"))
print(my_list3.count("python"))
new=[32 ,4 ,69,2 ,39,22]
print(sorted(new))
print(new)  #>>print unsorted
new.sort(reverse=True)
print(new)
new.reverse()
print(new)
my_new = new.copy()
print(my_new)
my_var=[1 , 3 ,4 ,"ali" , "omer"]
print(my_var)
print(type(my_var))