'''file=open("harry1.txt" , "a")
a= file.write("she has 3 brothers\n")
print(a)
file.close()'''
#to know the number of characters>>f.write()return this
#handle read and write mode
file=open("harry1.txt" , "r+")
print(file.read())
file.write("thanks")
file.close()