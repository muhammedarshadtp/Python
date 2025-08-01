# Child Without Its Own Constructor
 
class Animal:
    def __init__(self):
        print("ITs parent")

class Dog(Animal):
    def brak(self):
        print("Dog Barking")

a=Dog()

# Child Overrides Constructor

class A:
    def __init__(self):
        print("print A")

class B(A):
    def __init__(self):
        print("print B")   


c=B()


# Child Calls Parent Constructor Using super()


class School:
    def __init__(self):
        print("School")

class batch(School):
    def __init__(self):
        super().__init__()
        print("Batch")


a=batch()