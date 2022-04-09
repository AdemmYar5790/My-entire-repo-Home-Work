print('Enter data for writing in file: \nFor ending of writing enter empty string:')
with open('ex_1.txt', 'w', encoding='utf-8') as my_hw5:
    while (line := input()) != '':
        my_hw5.write(f"{line}\n")