class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    def __init__(self, value):
        self.value = value

# This will print "Creating class MyClass"
instance = MyClass(10)
