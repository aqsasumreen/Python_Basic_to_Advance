a=20
b=39
if a==b:
    print("equal")
elif a>b:
    print( "a greater than b")
else:
    print("b is greater")

#--->-NESTED

c = int(input("Enter value: "))
if c>=0:
     if c==0:
         print("value u entered is zero")
     else:
            print("value u entered is pos")
else:
     print("entered a -ve no")
#---------------------------------loops------------------------------
numbers =[2 ,4 ,7, 3 , 5]
sum=0
for i in numbers:
    sum+=i
#-->range fun
for i in range(10):
    print(i)

for i in range(2,7):
        print(i)

for i in range(1, 20 , 2):
            print(i)

#----------->for else

numbers =[2 ,4 ,7, 3 , 5]
sum=0
for i in numbers:
    sum+=i
    print(sum)
else:
    print("i is not present")

#---------->while loop

second=10
while second > 0:
    print(second , end= '->')
    second-=1
print("blastoff!")
counter = 0

while counter<3:
    print("hello")
    counter=counter+1;
else:
    print("why are you not replying")


# ********* FOR/ WHILE  ELSE

for i in range(5):
    print(i)
    if i == 4:
        break

# else:
#
#      print("loop ended successfully")
# 2
j = 0
while j < 8:
    print(j)
    if j==4: # jb hm loop break krty tou else nhi chly ga,, tbhi run hota jb sb iteration hogi
        break
    j += 1


# else:
#       print("loop ended successfully")