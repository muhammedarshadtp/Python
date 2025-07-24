  
 

for i in range(5):
    for j in range(5):
        print("#",end="")
    print() 

     #####
     #####
     #####
     #####
     ##### 

for i in range(5):
    for j in range(i+1):
        print("#",end="")
    print()    

    #
    ##
    ###
    ####

for i in range(5):
    for j in range(5-i):
        print("#",end="")
    print()    

    #####
    ####
    ###
    ##
    #

rows=5

for i in range(1,rows + 1):
    space=rows-i
    star=2*i-1
    print(" " * space + "*" * star)
