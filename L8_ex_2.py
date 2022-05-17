class DivisionByZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def div_by_null(divider, denominator):
        try:
            return (divider // denominator)
        except:
            return (f"Division by 0 is not allowed!")


div = DivisionByZero(10, 50)
print(DivisionByZero.div_by_null(10, 0))
print(DivisionByZero.div_by_null(10, 0.1))
print(div.div_by_null(100, 0))