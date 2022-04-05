def my_func(arg1, arg2, arg3):
    print(f'The Sum. of the two largest arguments is: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')

my_func(
    int(input('Arg. 1: ')),
    int(input('Arg. 2: ')),
    int(input('Arg. 3: ')),
)

