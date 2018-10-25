#Program to illustate scoping in Python
def f(x):
    print("In function f:")
    x+=1
    y=1
    print('x is', x)
    print('y is', y)
    print('z is', z)
    print('a is', a)
    print('b is', b)
    print('c is', c)
    return x
x, y, z, a, b, c = 5, 10, 15, 20, 25, 30

print('Before function f:')
print('x is', x)
print('y is', y)
print('z is', z)
print('a is', a)
print('b is', b)
print('c is', c)

b = f(x)
print('After function f:')
print('x is', x)
print('y is', y)
print('z is', z)
print('a is', a)
print('b is', b)
print('c is', c)
