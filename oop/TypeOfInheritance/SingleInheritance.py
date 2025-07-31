
class Animal:
    def sound(self):
        print("Animal make sound")

class dog(Animal):
    def bark(self):
        print("dog is barking")



d=dog()
d.sound()
d.bark()