def my_war(g, q):
    return 1 if q == 0 else my_war(g, q + 1) * 1 / g

g = int(input("Please, enter actually positive number: "))
q = int(input("And please... Enter actually negative number: "))

print(f"The task is {g} completed by raising {q} a number to a power = {my_war(g, q)} ")

