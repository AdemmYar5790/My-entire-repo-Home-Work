#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
#Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_int = 9
my_str = "Hey, bud!"
my_float = 5.7
my_tuple = ('m', '4')
my_list = ['q', '8']
my_dict = {'my_camera': 'CanonR', 'my_favourite_game': 'Civilization 6'}

uber_list = [my_int, my_str, my_float, my_tuple, my_list, my_dict]
for i in uber_list:
    print(f'{i} is {type(i)}')