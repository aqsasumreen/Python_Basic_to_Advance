import os
print(os.name)

# Get the list of all files and directories in the root directory
# print(os.listdir("/"))

# Get the current working directory
print(os.getcwd())

# Create a new directory
# os.mkdir('test_directory')
os.chdir('/django') #chg python to django
print(os.getcwd())
for i  in range(0,5):
     os.mkdir(f'django/day{i+1}')  # This will create a folder in the 'django' directory named 'day1', 'day2', etc.
     os.mkdir(f'/tut{i + 1}')      # This will create a folder in the E: drive named 'tut1', 'tut2', etc.
     os.makedirs(f'test_directory{i+1}') # This will create a folder in the 'django' directory named 'test_directory1', 'test_directory2', etc.
     os.rename(f'/tut{i + 1}', f'/del{i + 1}') # This will rename the folder from 'tut1' to 'del1', 'tut2' to 'del2', etc.
     print(os.name)

# folders = os.listdir("django") #in django folder further django
for f in folders:
# supp for a condition :
      if f.endswith(".py"):
        print(f)
        print(os.listdir(f' django/{f}'))













