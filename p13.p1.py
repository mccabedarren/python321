#Program that prints the largest of two user-entered numbers
#the the function "max"

def max(a,b):
    if a>b:
        return a
    else:
        return b
#prompt the user for two numbers

number_1 = float(input("Enter a number: "))
number_2 = float(input("Enter a number: "))

biggest = max(number_1,number_2)

print('The largest of', number_1,'and', number_2,'is', biggest)
print('Finished')
