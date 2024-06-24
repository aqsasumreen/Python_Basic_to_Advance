# The format() function in Python is a versatile and powerful method for
# formatting strings. It allows you to embed expressions inside string literals
# using curly braces {} and specify how values should be presented.
# The format() function is part of the str class and can handle complex
# formatting needs.

# Basic Syntax : "string".format(value1, value2, ...)

users = ['Ali','Omer','Sana','Saba','Ayesha','Aqsas']
computer = ['Mbl','Laptop','Andriod','Iphone','Linux','Mac']
for i in range(0 , len(users)):
    print("{}".format(computer[i]),"used by {}".format(users[i]))
