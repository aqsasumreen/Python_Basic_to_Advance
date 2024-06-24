# strings are immutable
#----> str splicing
my_str ="welcom to data science"
print(my_str[:])
print(my_str[2:10])
print(my_str[0:15:2])
print(my_str[::-1])
print(my_str[-7:-1])

# ****************String metthods****************

str = "this is my string!!!!!!!!!!!!"
print(str.lower())
print(str.upper())
print(str.isupper())  #false
print(str.isupper()) #false
print(str.capitalize()) #first letter capital
print(str.casefold()) #all in lower case
print(str.center(50)) #	Returns a centered string
print(str.count("my")) #Returns the number of times a specified value occurs in a string
print(str.index("my"))
print(str.find("my"))
print(str.startswith("is")) #false
print(str.endswith("ing")) #true
print(str.isalpha())
print(str.isalnum())
print(str.isprintable()) #Returns True if all characters in the string are printable
print(str.istitle()) #Returns True if the string follows the rules of a title
print(str.strip("!!!!!!!!!!!")) #Returns a trimmed version of the string
print(str.swapcase()) #Swaps cases, lower case becomes upper case and vice versa
print(str.split(" "))
print(str.title()) #Converts the first character of each word to upper case

