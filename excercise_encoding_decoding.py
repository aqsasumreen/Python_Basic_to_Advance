# ========================> Exercise Example 4 <============================

opt = input("Want to encode or decode: ")
str = input("Enter string: ")
words = str.split(" ")
if(opt == "encode"):
        nwords =[]
        for word in words:
            if(len(word) >= 3):
                r1= "abc"
                r2= "ghi"
                newStr  = r1 + word[1:]  + word[0] + r2
                nwords.append(newStr)
            else:
                 nwords.append(word[::-1])
        print(" ".join(nwords))

elif(opt == "decode"):
    nwords =[]
    for word in words:
        if(len(word) >= 3):
            r1= "abc"
            r2= "ghi"
            newStr  = word[3:-3]
            newStr = newStr[-1] + newStr[:-1]
            nwords.append(newStr)
        else:
             nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    print(" No string ")