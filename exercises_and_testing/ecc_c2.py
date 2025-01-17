import sys
sys.path.append('../btc')
from FieldElement import FieldElement
from Point import Point

if __name__=="__main__": 
    # point stuff
    # C2, E1, let curve be: y^2 = x^3 + 5a + 7
    a = 5
    b = 7
    # p1 = Point(x=2, y = 4, a=a, b=b)  # point not on curve
    p2 = Point(-1, -1, a, b)    # point on curve
    p3 = Point(18, 77, a, b)
    # p4 = Point(5, 7, a, b)    # point not on curve

    print(p2.on_curve(p3.x, p3.y)) # true
    print(p2.on_curve(1, 1)) # false

    # C2, Point Addition
    p1 = Point(-1, -1, 5, 7)
    p2 = Point(-1, 1, 5, 7)
    inf = Point(None, None, 5, 7)
    print(p1)
    print(p1 + inf)     # p1 + identity
    p_at_inf = p1 + p2      # vertical line, 3rd point is point at inf

    # C2,E5 Point Addition where x1 != x2
    p1 = Point(-1, -1, a, b)
    p2 = Point(2, 5, a, b)
    p3 = p1 + p2    # (3, -7)
    