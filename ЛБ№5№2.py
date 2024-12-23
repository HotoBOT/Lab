class Circle():

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self):
        self.radius = int(input("Введите новый радиус: "))

a = Circle(10)
print(a.get_radius())
a.set_radius()
print(a.get_radius())