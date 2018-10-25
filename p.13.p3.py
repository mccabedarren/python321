#program to print the largest of two user-entered numbers
#Uses two functions "max" and "print_max"

def print_max():
    def max(a,b):
        if a>b:
            return a
        else:
            return b
#prompt the user for two numbers

    number_1 = float(input("Enter a number: "))
    number_2 = float(input("Enter another number: "))

    print ("The largest of",number_1, "and", number_2, "is", max(number_1,number_2))
    return

print_max()
