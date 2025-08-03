
#----- Generator function:-------

# def squre(list):
#     for i in list:
#         yield i*i

# a1=squre([1,2,3,4])

# print(next(a1))



def count(n):
    count=1
    while count <= n :
        yield count
        count += 1



for i in count(4):
    print(i)