my_list = [55, 113, 567, 456677, 44, 1798, 56]
for i in range(len(my_list) - 1):
    g = [my_list[i]]
    i += 1
    q = [my_list[i]]
    if q > g:
        g = q
        print(q, end='')