
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

#  --------------   Tuples  -----------------

# num = ("apple")
# print(num)

#  -------------- Dictionary  --------------


# person = {
#     "name":"Arshad",
#     "age":24,
#     "city":"Kannur"
# }
# print(person)

#   ---------- Access Value  -------------

# print(person["city"])

# -------------- change value ------------------

# person["age"]=26
# print(person.get("age"))

#   -------------- add key-value pair  ----------------

# person["email"] = "arshad@gmail.com"
# print(person.get("email"))

#   -------------- remove key  ----------------

# person.pop("city")
# print(person)

#     #check if check key Exits

# if "name" in person:
#  print("yes")

#    -------------- Dictionary Methods ------------

# print(person.get("age"))
# print(person.keys())
# print(person.values())
# print(person.items())
# print(person.pop("age"))


#    ------------ Zip()  ------------

# key = ["name","age","place"]
# value=["arshad",24,"ulikkal"]

# zipped=dict(zip(key,value))
# print(zipped)

#     ------------- import math ------------

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
#       -----------User input in python --------------

# a=int(input("enter the 1st number"))
# b=int(input("enter the 2st number"))
# z= a-b
# print(z)

# a=input('enter the character')[1]
# print(a)

#    -------------- If elif Else  ----------


# a=3
# if a>5:
#     print("this is biggest")
# else:
#     print("this is smallest")    

# age=24

# if age<18:
#     print("your are a minor")
# elif age<25:
#     print("your are a adult")    
# else:
#     print("your are a senior citizen")    


#     ----------   while loop in python -------------

# a=1

# while a<=10:
#     print(a)
#     a=a+1


# i=1
# total = 0

# while i<=5:
#   total+=i
#   i+=1

# print("sum:",total)

# i=1
# num=4

# while i<=10:
#     print(i,"x",num, "=",num*i)
#     i+=1

# user_input = ""

# while user_input != "exit":
#     user_input = input("Type something (or 'exit' to stop): ")

#       ---------- for loop in python ------------

# x=[1,4,78,3,6,8,9,0,]
# for i in range(10,15,1):
#     print(i)

# for i in x:
#     if i%2==0:
#         print("this is an even number:",i)
#     else:
#         print("this is an odd number:",i)    

# ---------------- Break ---------------

# av=5

# x=int(input("how many item do you want?"))

# i=1

# while i<=x:

#     if i >av:
#         print("out of item")
#         break
#     print("Hey items")
#     i+=1
# print("byee")

# ----------- Continue ----------

# for i in range(1,10):
#     if i%3==0:
#         continue
#     print(i)

# -------------- Pass ------------


# for i in range(1,10):
#     if i%2 != 0:
#         pass
#     else:
#         print(i)
# print("byee") 
# 
# --------------- Pattern Printing in Python  --------------    

# for i in range(5):
#     for j in range(5):
#         print("#",end="")
#     print() 

#     output=  
#      #####
#      #####
#      #####
#      #####
#      ##### 

# for i in range(5):
#     for j in range(i+1):
#         print("#",end="")
#     print()    

#     output=
#     #
#     ##
#     ###
#     ####

# for i in range(5):
#     for j in range(5-i):
#         print("#",end="")
#     print()    

#     #####
#     ####
#     ###
#     ##
#     #