#--------> Sets are mutable

s2 = {"pak", "ind", "china", "bangla", "dubai"}
s3 = {"bangla", "pak", "ind"}
print(s2.union(s3))
print(s2)
s2.update(s3) # update the s2 values
print(s2.intersection(s3))
s2.intersection_update(s3) # update the s2 values
print(s2)
print(s2.symmetric_difference(s3))#symmetric difference is AuB - A intersection B
print(s2.difference(s3))
print(s2.isdisjoint(s3)) # if no common value then True
print(s2.issuperset(s3)) # each element of s3 present in s2 then True
print(s3.issubset(s2))
s3.add("Kabul")
print((s3))
s3.remove("bang") # if this elem is not present then show error
print(s3)
s3.discard("pakhxbjv") # f this elem is not present then will not show  error
print(s3)
print(s3.pop()) # pop new element at each run
del s3 # delete the complete set
print(s3.clear())
print(s3)


#--->operators with set

set1={1,3,4,6}
set2={3,4,9,8}
superset = {1 ,2 ,3 ,4, 5, 56}
s1={1,2,3,4}
s2={5,6,7,8}
print(s1==s2)
print(s1!=s2)
print(s1<=superset)
print(s1<superset)
print(s1>=s2)
print(s1>s2)

#--->assingment operator
'''a=6
div , rem ,expo = 1,1,1
#>>add , sub , mul
div/=a
print(div)
rem%=a
print(rem)
expo **=a
print(expo)'''
#--->logical operator
'''a=8
b=0
print(a and b)
print(a or b)
print( not b)'''
#--->bitwise operator
'''c = 3
d = 5
print(c & d)
print(c | d)
print(c ^ d)
print(~ d)   # >>will give neg
print(c << d)
print(c >> d)  #>>0'''
#--->identity operator
'''a={342 , 5, 55 }
b={7,3,2}
print(a is b)
print(a is not b)'''
#--->memebership operator
a= {2 , 5 ,8}
print(3 in a)
print(3  not in a)


