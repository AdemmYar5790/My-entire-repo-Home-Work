#Задача3: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input("Enter number: ")
g = int(number + number)
q = int(number+number+number)
summa = int(number) + g
summa1 = int(number) + g + q
summa2 = int(number) + g + q + g
print(summa)
print(summa1)
print(summa2)