class Worker:

    name = "Robert"
    lastname = "Bern"
    position = "Beautician"
    income = 55000
    bonus = 14000
    _income = {"Income": income,
               "Bonus": bonus
               }
    total_profit = 0


class Position(Worker):
    def get_full_name(self):
        return "{} \"{} {}\"".format(self.position, self.name, self.lastname)

    def get_full_profit(self):
        self.total_profit = self.income + self.bonus
        return ", income with bonus: {}".format(self.total_profit)


w = Worker()
print(w.name)
print(w.lastname)
print(w.position)
print(w.income)

p = Position()
print("\n<< General information about worker >> ")
print(p.get_full_name() + str(p.get_full_profit()) + " " + str(w._income))