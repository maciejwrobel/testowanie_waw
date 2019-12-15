class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def change_color(self, color):
        self.color = color

car = Car("BMW", "black")
car.change_color("red")
