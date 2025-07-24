
# def greet():
#     print("hello World")

# greet()


# def add(a,b):
#     c= a*b
#     print(c)
# add(4,5)

#   ---------Keyword variable length arguments---

# def person(name,**data):
#     print(name)
#     for i,j in data.items():
#         print(i,j)
# person("arshad",age=34,city="kannur",mob=123456789)   
# 

# ------passing list in function ---------

# lust=[2,1,3,4,5,6,7,8,9] 

# def count(lust):
#     odd=0
#     even=0
#     for i in lust:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#     return odd,even


# even,odd=count(lust)
# print("even: {}, odd:{}".format(even,odd))