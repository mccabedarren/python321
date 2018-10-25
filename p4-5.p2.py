import math

length = int(input('enter a length: '))
width = length

area_of_square = length * width

if area_of_square > 0:
    print ('area of square:' , area_of_square)
else:
    print ('area of square: length must be >0. Plase try again.')

volume_of_cube = area_of_square ** 2

if volume_of_cube > 0:
    print ('volume of cube:', volume_of_cube)
else:
    print ('volume of cube: length must be > 0. Please try again.')



area_of_circle = math.pi * 71761.5 ** 2

if area_of_circle > 0:
    print ('area of circle:', area_of_circle)
else:
    print ('area of circle: length must be > 0. Please try again.')


volume_of_sphere = 4/3 * math.pi * 71761.5 **3

if volume_of_sphere > 0:
    print ('volume of sphere:', volume_of_sphere)
else:
    print ('volume of sphere: length must be > 0. Please try again.')



volume_of_cylinder = math.pi * 71761.5 **2 *143523

if volume_of_sphere > 0:
    print ('volume of cylinder:', volume_of_cylinder)
else:
    print ('volume of cylinder: length must be > 0. Please try again.')

print ('Finished')
