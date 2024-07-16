class LogMixin:
    def log(self, message):
        print(f'LOG: {message}')

class MyClass(LogMixin):
    def do_something(self):
        self.log('Doing something!')

obj = MyClass()
obj.do_something()
# Output: LOG: Doing something!




