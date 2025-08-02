
class A:
    def a(self):
        print("i am A")

class B:
    def a(self):
        print("i am B")

def C(D):
    D.a()



C(A()) 
C(B())   