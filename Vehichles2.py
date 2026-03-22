class Vehichle:
    def __init__(self,capacity):
        self.capacity=capacity

    def cost(self):
        cost=1.1*100*self.capacity
        print('\nCalculating Cost:')
        print('$',int(cost))
        print()
    
class Bus(Vehichle):
    def __init__(self,capacity):
        super().__init__(capacity)
    
School_Bus=Bus(50)
School_Bus.cost()