#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, весна,
#лето, осень). Напишите решения через list и dict.

number_of_month = int(input("Enter number of month: "))
if number_of_month <= 12 and number_of_month >= 1:
    month_dict = {1: 'January',
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June',
                  7: 'Jule',
                  8: 'August',
                  9: 'September',
                  10: 'October',
                  11: 'November',
                  12: 'December'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number_of_month - 1 :
            print(f"Month from list: {month_list[i]}")
            break
    print('-------------------------------------------------------------------------------------------')
    print('and')
    print('-------------------------------------------------------------------------------------------')
    print(f"Month from dict: {month_dict[number_of_month]}")
else:
    print("You could be wrong(((")
print('-------------------------------------------------------------------------------------------')
print("Yaaaay!")
print('--------------------------------------------------------------------------------------------')
print('Thanks for playing!')
print('|||||+|||||+|||||+|||||+|||||+|||||+|||||+|||||+|||||+|||||+|||||+|||||+|||||+|||||+|||||+|||||')