

class outer:
    class inner:
        def greet(self):
            print("hello this is inner")


inner_obj=outer.inner()

inner_obj.greet()



class laptop:

    def __init__(self,brand):
        self.brand=brand
        self.battery=self.Battery()


    def show(self):
        print(f"Laptop brand is {self.brand}")
        self.battery.Get_Show()

    class Battery:

        def __init__(self):
                self.capacity="5000mAh"

        def Get_Show(self):
                print(f"Battery capacity is {self.capacity}")    


Lap=laptop("Dell")

Lap.show()
