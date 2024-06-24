# Warlus operator : The walrus operator (:=) in Python is a new assignment
# expression introduced in Python 3.8. It allows you to assign values
# to variables as part of an expression. This can be useful for
# simplifying code by reducing redundancy and improving readability.

# happy = True
# print(happy)
# print(happy := False)  # := assigns value to var as part of larger expression
foods = list()
# while True:
#     food = input("food do you like?")
#     if food == "quit":
#         break
#     foods.append(food)
#
# print(foods)

# 2 using warlus operator
while (food := input("food do you like? ")) != "quit":
    foods.append(food)

print(foods)