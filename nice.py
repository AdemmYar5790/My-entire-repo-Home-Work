print('-------------------------------------------------------------------------------------------')
game = int(input('Enter your number of game: '))
print('-------------------------------------------------------------------------------------------')
if game <= 8 and game >= 1:
    game_dict = { 1: 'Resident Evil: Village',
                  2: 'Dark Souls 2',
                  3: 'Civilization 6',
                  4: 'Doom: Eternal',
                  5: 'The Elder Scrolls',
                  6: 'Minecraft',
                  7: 'No Mans Sky',
                  8: 'Rust'}
    game_list = list(game_dict.values())
    for i, gm in enumerate(game_list):
        if i == game - 1:
            print(f"Game from list is: {game_list[i]}")
            break
    print('-------------------------------------------------------------------------------------------')
    print('and')
    print('-------------------------------------------------------------------------------------------')
    print(f"Game from dict is: {game_dict[game]}")
else:
    print("You could be wrong(((")
print('-------------------------------------------------------------------------------------------')
print("My congrats! Good choice!")