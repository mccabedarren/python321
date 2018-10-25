#Define function " Fibonacci" (Function to count the number of integers in a fibonacci sequence)
     #"Fibonacci" checks if the given limit is 1,2 or greater
     #If greater than 2 "Fibonacci" calculates the fibinonacci sequence while counting the number of factors
     #"Fibonacci" returns the count of integers in the fibonacci sequence
# the program takes input on the limit required
#if positive the program calls the function "Fibonacci"
#if negative the program prints the error message: "Error: Number must be greater than 0"


def fibonacci(limit):
    f_0 = 0
    f_1 = 1
    count = 0


    if limit <=0:
        print('Error: Number entered was less than or equal to 0')
    elif limit == 1:
        print ('Count is 1')
    elif limit ==2:
        print ('Count is 1')
    else:
    
       a = f_0
       b = f_1

       for i in range (2,limit):
          fib = b+a
          count +=1
        

          a=b
          b=fib
    
    return ('Count is:',count)

limit = int(input('enter the number of terms you want to calculate(an int >0): '))
if limit > 0:
    print (fibonacci(limit))
else:
    print ("Error: Number must be greater than 0")
