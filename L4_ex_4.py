lists_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
lists_2 = [r for r in lists_1 if lists_1.count(r) == 1]
print(lists_2)