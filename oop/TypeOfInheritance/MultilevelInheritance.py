
class A:
    def first(self):
        print("Frist")
class B(A):
    def Second(self):
        print("Second")
class C(B):
    def Thrid(self):
        print("Thrid")                


c = C()

c.first()
c.Second()
c.Thrid()