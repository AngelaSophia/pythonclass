class Car:
    brand="Mazda"
    def __init__(self,color,registor,speed):
        self.color=color
        self.registor=registor
        self.speed=speed
    def hoot(self):
        return f"Hello, my color is {self.color}"  
    def new_speed(self):
        return f"Hello,the speed is{180-self.speed}"