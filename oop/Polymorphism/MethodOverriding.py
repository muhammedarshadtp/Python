
class A:
    def show(self):
        print("Print A")
class B(A):
    print("show B")


ab=B()
ab.show()