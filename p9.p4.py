#prompt user for a number
#calculate the factorial using a while loop
#repeat until a negative number is entered


x = int(input('Enter a number'))

while x >= 0:
    
    if x == 0:
        fact = 1
    elif x == 1:
        fact = 1
    else:
        fact = 1
        i = 1
        while i <=x:
            fact*=i
            i+=1
    print ('Factorial of',x,'is',fact)
    x = int(input('Enter a number'))
