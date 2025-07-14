
# print('Hello world')

# print(3 + 3)

# x = 10

# print(x + 20)

# print(x+12)

# name = 'youtube'
# print(len(name))

# fruit =["apple","banana","Mango"]
# del fruit[1:]
# print(fruit)

#        Tuples

# num = ("apple")
# print(num)

#     Dictionary


# person = {
#     "name":"Arshad",
#     "age":24,
#     "city":"Kannur"
# }
# print(person)

#      # Access Value

# print(person["city"])

#       # change value

# person["age"]=26
# print(person.get("age"))

#     # add key-value pair

# person["email"] = "arshad@gmail.com"
# print(person.get("email"))

#     # remove key

# person.pop("city")
# print(person)

#     #check if check key Exits

# if "name" in person:
#  print("yes")

#     Dictionary Methods

# print(person.get("age"))
# print(person.keys())
# print(person.values())
# print(person.items())
# print(person.pop("age"))


#       Zip()

# key = ["name","age","place"]
# value=["arshad",24,"ulikkal"]

# zipped=dict(zip(key,value))
# print(zipped)

#      import math 

# a= math.sqrt(23)
# print(a)

# a=5
# b=6

# print(a)
# print(b)

# temp=a
# a=b
# b=temp
# print(a)
# print(b)

# a=a+b
# b=a-b
# a=a-b
# a,b=b,a
# print(a)
# print(b)
#       User input in python 
# a=int(input("enter the 1st number"))
# b=int(input("enter the 2st number"))
# z= a-b
# print(z)

# a=input('enter the character')[1]
# print(a)

# If elif Else

# a=3
# if a>5:
#     print("this is biggest")
# else:
#     print("this is smallest")    

age=24

if age<18:
    print("your are a minor")
elif age<25:
    print("your are a adult")    
else:
    print("your are a senior citizen")    