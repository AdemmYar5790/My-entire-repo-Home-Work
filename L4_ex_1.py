def bene():
    g = float(input('Please, enter a hours worked: '))
    q = float(input('Enter sum of hourly benefit: '))
    h = float(input('Enter sum of the premium: '))
    ben = g * q
    return ben + h

print("Name of this program is... 'The program of calculation a employee benefits from work'")

print(f'Value of employee benefits is: {bene() }')