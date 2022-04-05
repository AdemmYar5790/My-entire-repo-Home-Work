def total_sum():
    total_zum = 0
    while True:
        user_numbers = input("Enter a numbers, or input 'g' for break: ").split()
        for nums in user_numbers:
            if nums.lower() == "g":
                return total_zum
            else:
                try:
                    total_zum += int(nums)
                except ValueError:
                    print("For breaking of program enter 'g': ")
        print(f"Zum of numbers = {total_zum}")

print(total_sum())
