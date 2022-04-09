class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 100
        print(f'It is necessary to cover the entire roadway {round(asphalt_mass)} kg of mass of asphalt.')


r = Road(5000, 20)
r.asphalt_mass()