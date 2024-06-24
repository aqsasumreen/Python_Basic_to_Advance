# ********************* MATCH statement
x = int(input("Enter value for match:"))
match x:
    case 0:
        print("X is zero")
    case 1:
        print("X is one")

    case _ if x != 90:
        print("not a match")
    case _:
        print("default")

# **************** Continue ,  break

for i in range(12):
    if (i == 10):
        break
        continue
    print("break th iteration")
    print("5 X" , i ,"=" , 5*i)


print("break th loop")
print(" conitnue ,break the iteration")