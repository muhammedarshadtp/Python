
# ------------ Fibanacci in for loop--------

# def fib(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a)
#         a,b=b,a+b

# fib(10)

# --------Return Fibonacci as a List-------

# def fib(n):
#     result=[]
#     a,b=0,1

#     for i in range(n):
#         result.append(a)
#         a,b=b,a+b
#     return result


# print(fib(10))

# ------------Recursive Fibonacci (for learning only — not efficient) ------

# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
    
# for i in range(10):
#     print(fib(i))