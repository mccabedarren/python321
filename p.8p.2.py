table_size = int(input('Enter the size of the mulitplication table: '))

i = 1
while i <=table_size:
    j=1
    while j<= i:
        print(i * j,"",end = "")
        j+=1
    print()
    i+=1
