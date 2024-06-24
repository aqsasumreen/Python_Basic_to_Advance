#--------> basics of filing
'''
"r"-read mode- default
"w" _write
"x"-creats new file if alreay exits then it will not work
"a"- add more content to file
"t"- text mode -default
"b"- binary mode
"+"- read and write mode
#open in binary mode ,,rt>>open in txt mode
'''

file=open("harry.txt" , "rt" )
#content=file.read()   #>>if argument passed then it will read that number of character
#read character by character
'''for line in content:
    print(line)'''
#to print line by line we have to iterate file
'''for line in file:
    print(line , end="")'''
#read line function
print(file.readline())
print(file.readline())
#readlines()>>will store in list
# print(content)
file.close()