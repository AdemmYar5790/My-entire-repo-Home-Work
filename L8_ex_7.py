
class MyComplex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%s + %s)' % (self.a, self.b)

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return MyComplex(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.b * other.a + self.a * other.b
        return MyComplex(new_a, new_b)


q1 = MyComplex(6, 9)
g2 = MyComplex(8, 5)

print(f"{q1} + {g2} = ", q1 + g2)
print(f"{q1} * {g2} = ", q1 * g2)
