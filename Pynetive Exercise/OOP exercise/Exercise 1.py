from turtle import speed


class vehical:
    def __init__(self,max_speed,milage):
        self.milage = milage
        self.max_speed = max_speed
    def love(self):
        return (self.max_speed + self.milage)

car =  vehical(100,50)
print(car.max_speed,car.milage)
print(car.love())