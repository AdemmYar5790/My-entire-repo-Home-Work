# Задача 5: Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение
# прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчёте на одного сотрудника.

gain = int(input("Enter gain: "))
outlay = int(input("Enter outlay: "))
if gain > outlay:
    profitability = gain-outlay
    rentability = profitability/gain
    print(f"Great work! You have {profitability} profitability")
    worker = int(input("How many people work: "))
    print(f"{profitability/worker} for one worker! Nice!")
elif proceed == outlay:
    print("Hmmm... Not bad!")
else:
    print("Hell yeah!")