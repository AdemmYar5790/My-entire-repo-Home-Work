#5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У пользователя
#нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый 
#элемент с тем же значением должен разместиться после них.
from typing import List

list = [7, 5, 3, 3, 2]
while True:
    point = input('Please, enter random number: ')
    if not point.isdigit():
        print("Entered incorrect data. Try again!")
        continue
    else:
        point = int(point)
    gem = None
    for i, num in enumerate(list):
        if point > num:
            idx = i
            break
    if gem is None:
        list.append(point)
    else:
        list.insert(gem, point)

    print(list)
    gq = input('You done? Enter yes or no: ')
    if gq.lower() == 'yes':
        break