# from threading import *
# from time import sleep

# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             sleep(1)
# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hai")
#             sleep(1)

# a=A()
# b=B()

# a.start()
# sleep(0.2)
# b.start()
# a.join()
# b.join()

# print("outside")

import threading
import time

class Hello:

    def run(self):
        for i in range(5):
            print("Hello")
            time.sleep(1)

class Hai:
     def run(self):
        for i in range(5):
            print("Hai")
            time.sleep(1)

H1=Hello()
H2=Hai()

obj1=threading.Thread(target=H1.run)
obj2=threading.Thread(target=H2.run)

obj1.start()
time.sleep(0.2)
obj2.start()
obj1.join()
obj2.join()

print("Byee")