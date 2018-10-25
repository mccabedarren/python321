#prompt user for three ints (x,y,z)
#determine odd numbers
#print largest odd number ("The largest int is (x/y/z). It is odd.")
#if none are odd print ("None of the ints are odd")

print ("Enter three ints below (x,y,z)")

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

if x > y and z and x%2 != 0:
    print("x is greater than y and z, and is odd")
elif y > x and z and y%2 !=0:
    print("y is greater than x and z, and is odd")
elif z > x and y and z%2 !=0:
    print ("z is greater than x and y, and is odd")
elif x%2==0 and y%2==0 and z%2==0:
    print ("All three numbers you entered are even")
