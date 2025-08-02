
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
    
    def __str__(self):
        return f"{self.x},{self.y}"
        



d1=Point(1,2)
d2=Point(3,4)

result=d1+d2

print(result)



class Money:
    def __init__(self,amount):
        self.amount=amount


    def __add__(self,other):
        return Money(self.amount + other.amount)
    def __str__(self):
        return f"{self.amount}"


cash=Money(100)
cash1 = Money(200)

total= cash+ cash1
print(total)
        
        