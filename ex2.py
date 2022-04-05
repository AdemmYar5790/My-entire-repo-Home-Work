print()
print('__personal_info___')
print()
print('Please, wait...')
print()
print("Here we go!")
print()

def personal_info(name, lastname, year_of_birth, city, email, phone):
    return print(f'Yr_Name: {name} Yr_Lastname: {lastname} Yr_Birthday: {year_of_birth}'
                 f'Yr_City: {city} Yr_Email: {email} Yr_Phone_Number: {phone}')


personal_info(
    name=input('Name: '),
    lastname=input('Lastname: '),
    year_of_birth=input('Birthyear: '),
    city=input('City: '),
    email=input('Email: '),
    phone=input('Phone_Number: '),
)

print()
print("Thanks! Now we know more then you expect!)")
print()
print('Plese, wait. Oops! Your plastik cards are bloked)')
print()
print("Bye!.")
