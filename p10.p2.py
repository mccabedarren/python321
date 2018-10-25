#prompt user for a number
#calculate the cube root using exhaustive enumeration
#prompt user for another number
#end loop when zero is entered


number = int(input('Enter a number:'))
while number != 0:
    if number <0:
        new_number = -number
    else:
        new_number = number
    cube_root = 0
    while cube_root**3<new_number:
        cube_root+=1

    if cube_root **3 == new_number:
        if number < 0:
            cube_root = -cube_root
        print('Cube root of',number, 'is', cube_root)
    else:
        print(number,'is not a perfect cube')
    number = int(input('Enter a number:'))

