# -->List Comprehension

lis = [4, 45, 9, 81, 3]
print("the Divisible of 3" , [item for item in lis if item%3 ==0])
print([item **3 for item in lis if item%3!=0])

# The first print statement identifies and prints all numbers in the list that are divisible by 3.
# The second print statement identifies and prints the cubes of all numbers in the list that
# are not divisible by 3.

#--> dictionay Comprehension

dict_1  ={'a':3 , 'b':9 , 'A' :8 , 'B':10}
print({k.upper():dict_1.get(k.lower() , 0)+ dict_1.get(k.upper() , 0)   for k in dict_1.keys()})

# The key is k.upper().
# The value is the sum of the values associated with k.lower() and k.upper() in dict_1.

#--> Set  Comprehension

sqd = {x**2 for x in [4,6,3, 4]}
print(sqd)
# the resulting set will only include unique squared values.

#---> Generators comprehension
gen = (i for i in range(78) if i%3==0)
for item in gen:
    print(item)