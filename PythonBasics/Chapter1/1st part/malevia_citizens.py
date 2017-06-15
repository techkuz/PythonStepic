def half_perimeter(a, b, c):
    return (a + b + c) / 2
    
def herons_formula():
    a = int(input())
    b = int(input())
    c = int(input())
    p = half_perimeter(a, b, c)
    result = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
    print (result)


shape = input()

if shape == "треугольник":
    herons_formula()

elif shape == "прямоугольник":
    a = int(input())
    b = int(input())
    print (a * b)

elif shape == "круг":
    r = int(input())
    print (3.14 * r ** 2)