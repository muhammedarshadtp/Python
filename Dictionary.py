
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