# Syntax:
enumerate(iterable, start=0)


lis = ['Cwh' , 'Sentdex' ,'clever pro', 'Mosh','Yt','Codebasics','WScube','Tech']

i=0
for  item  in lis:
    i=i+1
    if i%2== 0:
        print(i ,item)


# Another way
for i , item in enumerate(lis):
    if (i+1) % 2 == 0:
        print(i, item)


# #with changing index
for i, item in enumerate(lis, start=1):
    if i % 2 == 0:
        print(i, item)


# Enumerate in list comprehension
indexed_lis = [(i, item) for i, item in enumerate(lis)]
print(indexed_lis)


# Output

[(0, 'Cwh'), (1, 'Sentdex'), (2, 'Clever Pro'), (3, 'Mosh'), (4, 'Yt'), (5, 'Codebasics'), (6, 'WScube'), (7, 'Tech')]