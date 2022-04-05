# Задача 4: Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

your_number = input("Enter your number: ")
x = 0
for i in your_number:
    while int(i) > x:
        x = int(i)
print(x)
print("Great work!")