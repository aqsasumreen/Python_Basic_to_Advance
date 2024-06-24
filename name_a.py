import  os
def function_1():
    print("Im a name_a file")

# function_1() # This should run automatically when imported into the 'name_b' file, no need to call it explicitly.
print(__name__)
def main():
    print(os.listdir("/"))
if (__name__ == "__main__"):
    main()


# If function_1() is not called here, it won't run on its own in another file.
# If we keep this extra data simply in a function instead of an 'if' statement,
# we can also call it in another file.
    