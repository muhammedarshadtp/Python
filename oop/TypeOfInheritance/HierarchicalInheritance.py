

class Vehicle:
    def Start(self):
        print("Vehile Start")
class Car(Vehicle):
    def Drive(self):
        print("Car Starting")
class Bike(Vehicle):
    def ride(self):
        print("Bike ride")


c=Car()
b=Bike()
c.Start()
b.Start()                        