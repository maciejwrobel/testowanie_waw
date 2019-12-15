from klasy import Car

def test_car_init():
    car = Car("BMW", "black")
    assert car.name == "BMW"

def test_car_change_color():
    car = Car("BMW", "black")
    car.change_color("red")
    assert car.color == "red"
