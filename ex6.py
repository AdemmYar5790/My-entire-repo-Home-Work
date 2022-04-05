def text_func():
    for text in input("Plese, enter your imagency words across space (Preferably in latin low letters):\n").split():
        symbols = 0
        for symbol in text:
            if 97 <= ord(symbol) <= 122:
                symbols += 1
        print(text.title() if symbols == len(text) else f"{text} ")

text_func()