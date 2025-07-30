
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


class BankAccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance


    def deposite(self,amount):
        self.balance+=amount
        print(f"{self.name} deposited ₹{amount}. New balance is ₹{self.balance}")    


    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} withdrew ₹{amount}. Remaining balance is ₹{self.balance}")
        else:
            print("Insufficient balance!")    

    def balanceCheack(self):
        print(f"{self.name}'s account balance is ₹{self.balance}")
    


account=BankAccount("Arshad",1000)

account.deposite(500)
account.withdraw(200)
account.balanceCheack()