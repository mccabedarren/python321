year = int(input("enter a year:"))

print("Year entered:",year)

if year >=0:
    if (year%4==0 and year%100!=0
            or year%400 ==0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
else:
    print ("Year must be greater than 0")
print ("Finished")
