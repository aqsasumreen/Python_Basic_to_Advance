# Context managers are a powerful feature in Python that manage the setup and
# teardown of resources automatically. They are commonly used for handling
# resource management tasks such as opening and closing files, acquiring and
# releasing locks, and connecting and disconnecting network connections.


#-->Using Context Managers with with Statement
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# In this example, the file is opened and read within the with block,
# and it is automatically closed when the block is exited, even if an exception occurs.

# -->Creating Custom Context Managers
# You can create custom context managers by defining a class with __enter__ and __exit__ methods
# or by using the contextlib module.
#
#-> Using a Class with __enter__ and __exit__ Methods:
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

# Usage
with MyContextManager() as manager:
    print("Inside the context")


#-> Using the contextlib Module:
# The contextlib module provides a convenient way to create context managers using
# a generator function.

from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering the context")
    yield
    print("Exiting the context")

# Usage
with my_context_manager():
    print("Inside the context")

# --------->Real-World Examples<-------------
# File Handling:
with open('data.csv', 'r') as file:
    data = file.read()
    # Process the data

# Database Connections:
import sqlite3

with sqlite3.connect('example.db') as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM table')
    results = cursor.fetchall()
    # Process the results

# Thread Locks:

import threading

lock = threading.Lock()

with lock:
    # Critical section of code
    print("Thread-safe operation")

