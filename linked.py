
#
#
# main_list = [1, 2, 3]
# sub_list = ['a', 'b', 'c']
# main_list.insert(1, sub_list)
# print(main_list)

# Output:
# A-  [['a', 'b', 'c'], 1, 2, 3]
# B-  [1, ['a', 'b', 'c'], 2, 3]
# C- [1, 'a', 'b', 'c', 2, 3]

# done
str = "this is my  string"
print(str.title())

#  --Options--
# a) THIS IS MY STRING
# b) This is my string
# c) This Is My String


# tup1 = (7, 8, 9, 12)
# tup1[1] = "tuple"
# print(tup1)


#  -- Options --
# a) (7, "tuple", 8, 9,12)
# b) Error
# c) ("tuple",7, 8, 9, 12)



def to_upper(k):
    return k.upper()

x = ['ab', 'cd']
# print(list(map(upper, x)))



# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension way
squares = [x**2 for x in range(10)]

print(squares)



# Old style
# print("Name: %s, Age: %d" % (name, age))
#
# # New style
# print("Name: {}, Age: {}".format(name, age))
#
# # f-strings (Python 3.6+)
# print(f"Name: {name}, Age: {age}")




# import re
#
# pattern = r'\b\w{4}\b'
# text = "This is a test text with some four-letter words."
# matches = re.findall(pattern, text)

# print(matches)  # ['This', 'test', 'text', 'with', 'some', 'four']





person = {'name': 'Alice', 'age': 25}
person.update({'age': 26, 'city': 'New York'})
# print(person)

#  Options
#A -- {'name': 'Alice', 'age': 26, 'city': 'New York'}
#B -- {'name': 'Alice', 'age': 25, 'city': 'New York'}
#C -- {'age': 26, 'city': 'New York'}
#D --  Error



from collections import namedtuple

# Define a named tuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# print(p.x, p.y)  # Output: 10 20



from collections import Counter

text = "hello world"
counter = Counter(text)

# print(counter)

# Output:
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

my_str = ""
not_str = not my_str
my_bool = True or False
print(my_bool == not_str)







