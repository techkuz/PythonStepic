def half_perimeter(a, b, c):
    return (a + b + c) / 2
    
def herons_formula():
    a = int(input())
    b = int(input())
    c = int(input())
    p = half_perimeter(a, b, c)
    result = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
    print (result)
    
herons_formula()