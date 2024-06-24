import random

user = input("Enter S , W or G ")

cpu1 = random.randint(0, 2)
cpu = ["S", "W", "G"][cpu1]


def match(cpu, user):
    if cpu == user:
        return "Noboady , match tied"
    elif cpu == "S" and user == "W":
        return "CPU"
    elif cpu == "S" and user == "G":
        return "User"

    elif cpu == "W" and user == "S":
        return "user"

    elif cpu == "W" and user == "G":
        return "CPU "
    elif cpu == "G" and user == "S":
        return "CPU"
    elif cpu == "G" and user == "W":
        return "User "


result = match(cpu, user)
print(f"CPU: {cpu}, User: {user}, Winner is {result}")
