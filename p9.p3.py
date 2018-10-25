#calculating the factorial
#prompt the user for a number
#calculate the factorial of this number using the FOR loop

x = int(input('Enter a number:'))

if x < 0:
    print('Number enter was less than 0. Number must be positive')
else:
    if x == 0:
        factorial = 0
    elif x == 1:
        factorial = 1
    else:
        factorial = 1
        for i in range (1, x+1):
            factorial*=i
    print('Factorial of',x,'is',factorial)
        
