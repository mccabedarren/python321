#Prompt the user for a number
#Use exhaustive enumeration to determine whether the number is a perfect square
#If it is, determine the square root


x = int(input('Enter the number for which you want to calculate the square root:'))

if x < 0:
    print ('Number must be positive')
    
square_root = 0
while square_root**2< x:
    square_root += 1
if square_root**2==x:
    if x <0:
        square_root = -square_root
    print('Square root of',x,'is',square_root)
else:
    print('Number is not a perfect square')
