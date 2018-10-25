#Program to print out the largest of two user-entered numbers
#Uses function "max" in a print statement

def max(a,b):
    if a>b:
        return a
    else:
        return b

#prompt the user for two floating-point numbers:

number_1 = float(input("Enter a number: "))
number_2 = float(input("Enter another number: "))

print ("The largest of", number_1,"and", number_2, "is", max(number_1, number_2))
print("Finished!")
        
