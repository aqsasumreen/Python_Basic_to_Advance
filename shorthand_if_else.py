# =======================> shorthand if-else <========================
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# ******* Hm chahty hy k for loop me jb index 3 ho tou certain msg show ho jaye********

# way one

marks = [20, 30, 40, 50, 60, 70]
index = 0
for mark in marks:
    print(mark)
if (index==3):
    print("hey! you good")
index = index + 1

# another way of doing this

for index, mark in enumerate(marks, start=1):  # index always stored in first value ,,
    print(mark)  # start=1 means to start with 2nd value which is mark
if index == 3:
    print("hey! you good")