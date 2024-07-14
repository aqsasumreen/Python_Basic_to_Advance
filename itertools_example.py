import itertools

list1 = [1, 2, 3]
list2 = ["YT", "FB", "SC"]
combined = list(itertools.chain(list1, list2))
print(combined)


# Output: [1, 2, 3, 'YT', 'FB', 'SC']
