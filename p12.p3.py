#Define function "sqroot" (Function to find the square root of input float)
   #"Sqroot" calculates the square root using a while loop
   #"Sqroot" gives the number of guesses taken to calculate square root
#The program takes input of a float
#if positive the program calls the function "sqroot"
#if negative the program prints the error message: "Error: Number must be greater than 0"


def sqroot(number):
    epsilon = 0.01
    step = epsilon**2
    numguesses=0
    root = 0.0
    while abs(number-root **2) >=epsilon and root <=number:
        root += step
        numguesses +=1
        if numguesses % 100000 == 0:
            print('Still running. Number of guesses:',numguesses)
    print ('Number of guesses:',numguesses)
    if abs (number-root**2) < epsilon:
        return ('The approximate square root of',number,'is',root)
    else:
        return('Failed to find the square root of',number)


number = float(input('Enter the number for which you wish to calculate the square root:'))
if number > 0:
    print (sqroot(number))
else:
    print("Error: Number must be greater than 0")
