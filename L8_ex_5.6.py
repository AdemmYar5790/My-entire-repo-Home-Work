class OfficeEquipment:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Model': self.name, 'Price for one thing': self.price, 'Amount': self.quantity}

    def income(self):
        try:
            name = input(f'Enter name: ')
            price = int(input(f'Enter price for 1 thing: '))
            quantity = int(input(f'Enter amount: '))
            item = {'Model:': name, 'Price for one thing': price, 'Amount': quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Unacceptable!')


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


p = Printer('Hp', 2, 300)
s = Scanner('Canon', 54000, 10)
x = Xerox('Xerox', 7000, 15)
p.income()
s.income()
x.income()