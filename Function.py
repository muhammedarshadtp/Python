
# def greet():
#     print("hello World")

# greet()


# def add(a,b):
#     c= a*b
#     print(c)
# add(4,5)

#   ---------Keyword variable length arguments---

def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person("arshad",age=34,city="kannur",mob=123456789)    