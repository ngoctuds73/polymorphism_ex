from abc import abstractmethod, ABC


class Vehicle(ABC):
    @abstractmethod
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.fuel_consumption_increase = 0

    def drive(self, distance):
        fuel_cost = (self.fuel_consumption + self.fuel_consumption_increase) * distance
        if self.fuel_quantity >= fuel_cost:
            self.fuel_quantity -= fuel_cost

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.fuel_consumption_increase = 0.9


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.fuel_consumption_increase = 1.6

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
