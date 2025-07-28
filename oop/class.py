
class computer:
    def config(com1):
        print("Hello world")


com1=computer()

com1.config()


class person:

    def __init__(self,name,age):

        self.name=name
        self.age=age

    def greet(self):

        print(self.name,self.age)
        

p1=person("arshad",24)

p1.greet()