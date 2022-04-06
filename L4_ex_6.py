def gen1():
    g = int(input('Введите стартовое число: '))
    from itertools import islice
    from itertools import count

    for i in islice(count(g), 6):
        print(i)
gen1()