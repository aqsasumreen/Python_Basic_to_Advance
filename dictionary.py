#mutable >> can be modified

my_dict  = {1:"ali"  , 2: "aqsa"}
my_dict2 = dict({3:"python" , 4:"java"})
print(my_dict)
print(my_dict2)

#-->acessing its elelments
print(my_dict2[3])
print(my_dict2.get(4))

#-->ADD AND CHANGE
my_dict[1] = 'sana'
print(my_dict)
my_dict2[5] = 'Ruby'
print(my_dict2)

#-->DELETING
a=my_dict2.pop(5)
print("\nvalue" , a)
print(my_dict2)
b=my_dict2.popitem() #>>car.pop("model")
print("\n key , value" , b)
print(my_dict2)
my_dict2.clear()
print(my_dict2)

#-->OTHER FUNCTIONS

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.get(2))

# for k,v in my_dictt.items():
#      print(k, v)

# for key in my_dict.keys():
#      print(f"The Value for the {key} is {dict[key]}" )

# METHODS-------------->>>
d1 = {2: "abc", 3: "def"}
d2 = {4: "ghi", 5: "jkl"}
# d1.update(d2)
# d1.clear()
# d1.pop(2)
# d1.popitem() # delet any item
# del d1[3] # if key is not given then it will delete the complete list
# print(d1)