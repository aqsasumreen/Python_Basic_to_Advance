# ==========================> Recursion<==========================
# Recursion in Python refers to a programming technique where a function
# calls itself directly or indirectly to solve a problem.
# It's a powerful concept in programming and is commonly used in scenarios
# where a problem can be broken down into smaller, similar subproblems.

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)


a = int(input("Enter number for factorial: "))
print(factorial(a))