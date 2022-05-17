class Matrix:
    def __init__(self, nums_1, nums_2):
        self.nums_1 = nums_1
        self.nums_2 = nums_2

    def __add__(self):
        matrix = [[0, 0],
                 [0, 0],
                 [0, 0]]

        for g in range(len(self.nums_1)):

           for q in range(len(self.nums_2[g])):
            matrix[g][q] = self.nums_1[g][q] + self.nums_2[g][q]

        return str('\n'.join(['\t'.join([str(q) for q in g]) for g in matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(q) for q in g]) for g in matrix]))

my_matrix = Matrix([[8, 13],
                    [5,78],
                    [55, 2]],
                   [[3, 47],
                    [9, 73],
                    [25, 99]])

print(my_matrix.__add__())

pass