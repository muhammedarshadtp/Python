from functools import reduce
#   =---------- Anonymous Functions | Lambda-----------

f= lambda a: a*a

result = f(5)

print(result)

#  -------------- Filter--------

nums=[1,2,3,4,5,6,7,8,9]

even= list(filter(lambda n : n%2==0,nums))
print(even)

# -----------Map-----

double = list(map(lambda n: n*2,even))

print(double)

#-----------Reduce------

sum = reduce(lambda a,b:a+b,nums)\

print(sum)