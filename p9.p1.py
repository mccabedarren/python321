#Calculating the sum of integers of a number
#prompt use for number: int(input('enter a number'))
#calculate sum of integers using while loop
#print('sum of integers of entered number is ...')



x = int(input('Enter a number:'))

if x<=0:
    print ('Number must be greater than 0')
else:
    i = 1
    y=0
    while i <=x:
        y+=i
        i+=1
print('Sum of integers of', x ,'is' ,y,)
