# tuples are immutable , to add new element in existing tupple , first chg tuple into list then append
# and then add new element
tup1 = ('Pak', 'Ind', 'Pak', 'china')
temp =list(tup1)
temp.append("russia")
tup1 = tuple(temp)

temp = ("russia")
tuples = temp + tup1
# print(tuples)
print(tup1.count("Pak"))
print(tup1.index("Pak"))
print(tup1.index("Pak" , 2 ,3))
tup2 = (3, 5, 6, 3 ,4, 3)
print(tup2.index(3,4,6))
