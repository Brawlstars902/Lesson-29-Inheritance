class Vehichle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(Vehichle):
    pass

School_bus=Bus('No.853',150,15)
print('\nThe name of this school bus is ',School_bus.name,', the maximum speed is ',School_bus.max_speed,', and the mileage is ',School_bus.mileage,'.\n')