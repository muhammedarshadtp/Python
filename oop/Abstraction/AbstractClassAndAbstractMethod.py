from abc import ABC,abstractmethod



class Animal(ABC):
    @abstractmethod
    def Sound(self):
        pass
    def sleep(self):
        print("sleeping")
class Dog(Animal):
    def Sound(self):
        print("Bark")  


a=Dog()
a.sleep()
a.Sound()
