class Stationery:

    def draw(self):
        print("Parent method is Class of Stationary ")


class Pen(Stationery):
    def draw(self):
        print("\nParent method is Class of Pen")
        print("Drawing started for Pen")


class Pencil(Stationery):
    def draw(self):
        print("\nParent method is Class of Pencil")
        print("Drawing started for Pencil")


class Handle(Stationery):
    def draw(self):
        print("\nParent method is Class of Handle")
        print("Drawing started for Handle")


s = Stationery()

s.draw()

pen = Pen()
pen.draw()

penc = Pencil()
penc.draw()

hand = Handle()
hand.draw()
