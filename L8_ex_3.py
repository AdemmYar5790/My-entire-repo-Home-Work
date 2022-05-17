class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Entering number and then tap the Enter: '))
                self.my_list.append(val)
                print(f'The current list: {self.my_list} \n ')
            except:
                print(f"Invalid value")
                y_or_n = input(f'Do you want try again? Yes or No? ')

                if y_or_n == 'Yes' or y_or_n == 'yes':
                    print(try_except.my_input())
                elif y_or_n == 'No' or y_or_n == 'no':
                    return f'Thanks'
                else:
                    return f'Thanks'


try_except = Error(1)
print(try_except.my_input())
