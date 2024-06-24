print("Hey I`m \"AQSA\" \n pursuing BSSE")

# ===========================> Custom Error <==============================
# a = int(input("Enter number between 5-9:   "))
# b = input("Enter string which must be Quit: ")
# if (a<5 or a>9 ) :
#     raise ValueError("Invalid number ")
# elif(b != "Quit"):
#     raise ValueError("invalid string")
#
# else :
#     print("all ok")

# ------------------------difference between "is" vs "=="---------------------------
# is -> compare exact location of onj in memory
# == -> compare the values
# jb hm koi immutable variable bnaty  suppose hm a, b ko same 3 dety ,, tou memory aik hi block
# bna k a,b ko point kr de gi ,,coz memory knows k ye nhi chg hny waly
c = [1, 2, 3]
d = [1, 2, 3]
# print(c is d)  # not  same location coz list is mutable
# print(c == d)

# --------------------------------------------------------------
#   DICTIONARIES ARE PYTHON ORDERED OBJECTS
# iterating aver a sequence is called traversal
# WHILE LOOP IS AN INFINITE LOOP
# WRITE A FUNCTION TO DOUBLE THE VALUES OF LIST
list_1 = [2,3,4,5,6]
def double(num):
    result =[]
    for i in num:
        result.append(i*2)
    print(result)

double(list_1)


# ----------------------------------------------------------------
def word_frquency(phrase):
    result ={}
    words = phrase.split()
    for word in words:
        if word not in result:
            result[word] =1
        else:
            result[word]+=1
    return result

print(word_frquency(input("Enter your Phrase")))



