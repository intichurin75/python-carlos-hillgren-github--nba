import math
def pythagoras(a,b):
    c2 = a*a + b*b
    c = math.sqrt(c2)
    return c

hypotenusan = pythagoras(3,4)
print(f"Triangelns hypotenusa är: {hypotenusan} längd enheter")

dir(math)