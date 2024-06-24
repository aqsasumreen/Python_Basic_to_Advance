'''from math  import pi
r=float(input("input the radius of circle:"))
print("the radius of the circle with radius"+str(r)+"is:"+str(pi*r**2)
   fname=input("input your first name:")
   lname=input("input your last name:")
   print("hello me" +" " +fname+" "+lname)
color_list=["red","green","white","black"]
print(color_list[1],color_list[2])'''

def list_count_4(nums):
    count=0
    for num in nums:
        if num==4:
            count=count+1


    return count
print(list_count_4([4,3,4,5,4]))