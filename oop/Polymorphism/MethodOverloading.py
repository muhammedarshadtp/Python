

# class student:

#     def batch(self):
#         print("first batch")

#     def batch(self,a):  # This will overwrite the first one!
#         print("second Batch")

# A=student()
# A.batch(4)

#------------ Default argument---------#


class greet:

    def show(self,name=None):

        if name:
            print(f"Hello {name}")
        else:
            print("Hello")  

A1=greet()

A1.show()
A1.show("Arshad")


##-------- variable argument----------#

class Math:

    def add(self,*args):
        return sum(args)

total = Math()
print(total.add(1,2,3,4,5))
print(total.add())

##---------- Manual arguments---------#


class printer:

    def print_type(self,data):
        if isinstance(data,int):
            print("integer:",data)
        elif isinstance(data,str):
            print("string:",data)   
        else:
            print("unknown type")


cls=printer()

cls.print_type(1)
cls.print_type("hello")
