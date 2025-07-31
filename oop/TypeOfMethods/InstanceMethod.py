
class student:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print(f"hello {self.name}")    

s1=student("Arshad")
s1.greet()