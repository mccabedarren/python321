table_size = 20

i = int(input('Enter a number: '))
while i <=table_size:
    j=0
    while j<= 20:
        print(j, i * j,"")
        j+=1
    print()
    break
print ('Finished')
