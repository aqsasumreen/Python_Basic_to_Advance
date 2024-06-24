import time
initial = time.time()
k =0
while k<10:
    print("This is Aqsa..")
    time.sleep(3)
    k+=1
print("While loop Ran in " ,time.time()-initial , "seconds")
initial2  = time.time()

for i in range(10):
    print("This is Mawo..")

print("For loop ran in", time.time() -initial2, "seconds")

t = time.localtime()
ft = time.strftime("%Y-%m-%d %H:%M:%S" ,t)
print(ft)


# ***********  TIME function

timeStamp = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
if 0 < hour < 12:
    print("Its morning..")
elif 12 < hour < 17:
    print("Its evening..")
elif 17 < hour < 24:
    print("Its evening..")
else:
    print("Its day..")