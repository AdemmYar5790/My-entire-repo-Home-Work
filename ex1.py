def delen(g, q):
    try:
        return g / q
    except ZeroDivisionError as р:
        print(f'Oops! Not divisible by Zero(')

print(delen(int(input('Yr First Num: ')), int(input('Yr Second Num: '))))



