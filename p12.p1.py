#define Function "Facto" (function to find the factorial of a number)
        #"Facto" checks if number is 0,1 or greater than 1
        #if number is 0 or 1 "Facto" returns a factorial of 1
        #if greater than 0 "Facto" calculates the factorial using a while loop
        #"Facto" returns "Factorial of "a" is "fact"
#the program takes input from the user in the form of a single integer
#the program checks if the number is positive or negative
#if positive the program calls the function "Facto"
#if negative the program prints the error message "Error: Number must be greater than 0"


def facto(a):
    if a == 0:
            fact=1
    elif a ==1:
            fact =1
    elif a > 1:
        fact = 1
        i = 1
        while i<=a:
                fact*=i
                i +=1
    return('Factoral of',a,'is',fact)
    
a = int(input('Input a single non-negative integer:'))
             
if a >0: 
     print (facto(a))
else:
    print ('Error: Number must be greater than 0.')
