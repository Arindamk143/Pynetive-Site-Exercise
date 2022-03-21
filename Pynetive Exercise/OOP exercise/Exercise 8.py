from cgi import MiniFieldStorage
import sched


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(f"This a the name of bus:\n {School_bus.name}\n also this bus speed is {School_bus.mileage}\n This Bus Passenger capacity is {School_bus.capacity}")
print(isinstance(School_bus, Vehicle))