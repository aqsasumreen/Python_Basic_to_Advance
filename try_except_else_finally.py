# The try block is used to enclose code that might throw an exception (an error).
try:
    open("this.txt")

# The except block catches and handles exceptions that occur in the
# corresponding try block.
except:
    print("no such file or directory")

# The else block is executed if the code in the try block does not raise
# an exception.
else:
    print("no Exception caught")

# The finally block is always executed after the try block, regardless
# of whether an exception was raised or not.
finally:
    print("code in this block must run.")
# ------------------------------------------------------------------------
def fun():
    try:
        l = [2, 3, 4, 5]
        k = int(input("Enter index for number to print: "))
        print(l[k])
    except:
        print("An error occurred")

    finally:
        print("\n I`m imp in function")


fun()