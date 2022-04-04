import math

def find_roots(a,b,c):
    l = []
    discriminant = (b * b) - (4 * a * c)
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant) / (2 * a))
        root2 = (-b - math.sqrt(discriminant) / (2 * a))
        l.append(root1)
        l.append(root2)
        r = tuple(l)
        return l
    elif discriminant == 0:
        root1 = root2 = -b / (2 * a)
        l.append(root1)
        l.append(root2)
        r = tuple(l)
        return r
    elif(discriminant < 0):
        root1 = root2 = -b / (2 * a)
        imaginary = math.sqrt(-discriminant) / (2 * a)
        l.append(root1)
        l.append(imaginary)
        l.append(root2)
        l.append(imaginary)
        r = tuple(l)
        return r

print(find_roots(2,4,2))