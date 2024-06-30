from FieldElement import FieldElement
from Point import Point

if __name__=="__main__": 
    # C1
    a = FieldElement(3, 31)
    b = FieldElement(24, 31)

    # check division
    div1 = 3 * pow(24, 31 - 2, 31) % 31
    print(div1)
    div2 = (a / b).num
    print(div1 == div2)

    # check exp
    a = FieldElement(7, 13)
    b = FieldElement(8, 13)
    print(a**-3)
    print(pow(7, 3, 13)**11 % 13)

    # point stuff
    # C2, E1, let curve be: y^2 = x^3 + 5a + 7
    a = 5
    b = 7
    # p1 = Point(x=2, y = 4, a=a, b=b)  # point not on curve
    p2 = Point(-1, -1, a, b)    # point on curve
    p3 = Point(18, 77, a, b)
    # p4 = Point(5, 7, a, b)    # point not on curve

    print(p2.on_curve(p3.x, p3.y))
    print(p2.on_curve(2, 4))