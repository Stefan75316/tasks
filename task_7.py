"""
What do you see here? What is happening here?
"""


class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None

    def __str__(self):
        return f"Car: {self.make} {self.model}, year: {self.year}, color: {self.color}"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_year(self, year):
        self.car.year = year
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def build(self):
        return self.car


car_builder = CarBuilder()
car = (
    car_builder.set_make("Mercedes-Benz")
    .set_model("A-class")
    .set_year(2022)
    .set_color("black")
    .build()
)

print(car)
