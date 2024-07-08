import sys
sys.path.append('../btc')
from FieldElement import FieldElement
from Point import Point

def exercise_1_on_curve(x, y, prime) -> bool:
    y_side = y**2 % prime
    x_side = (pow(x, 3, prime) + 7) % prime
    if y_side == x_side:
        return True
    return False
def get_order_of_point(p: Point):
    next_p = p + p
    order = 2
    point_at_inf = Point(None, None, p.a, p.b)
    while next_p != point_at_inf:
        order += 1
        next_p = next_p + p
        # print(next_p)
        
    return order

if __name__=="__main__": 
    # E1
    prime = 223
    # print(exercise_1_on_curve(192, 105, prime))
    # print(exercise_1_on_curve(17, 56, prime))
    # print(exercise_1_on_curve(200, 119, prime))
    # print(exercise_1_on_curve(1, 193, prime))
    # print(exercise_1_on_curve(42, 99, prime))

    # E2
    # prime = 223
    # a = FieldElement(0, prime)
    # b = FieldElement(7, prime)
    # x1 = FieldElement(192, prime)
    # y1 = FieldElement(105, prime)
    # x2 = FieldElement(17, prime)
    # y2 = FieldElement(56, prime)
    # p1 = Point(x1, y1, a, b)
    # p2 = Point(x2, y2, a, b)
    # p3 = p1 + p2
    # print(p3)
    # print(p3 + Point(x=FieldElement(60, prime), y=FieldElement(139, prime), a=a, b=b))
    # p1 = Point(FieldElement(47, prime), FieldElement(71, prime), a, b)
    # p2 = Point(FieldElement(17, prime), FieldElement(56, prime), a, b)
    # print(p1 + p2)
    
    # E4
    # prime = 223
    # a = FieldElement(0, prime)
    # b = FieldElement(7, prime)
    # p = Point(FieldElement(192, prime), FieldElement(105, prime), a, b)
    # for i in range(1):
    #     print(i)
    #     p = p + p
    # print(p)

    # E5
    prime = 223
    a = FieldElement(0, prime)
    b = FieldElement(7, prime)
    x0 = FieldElement(15, prime)
    y0 = FieldElement(86, prime)
    p0 = Point(x0, y0, a, b)
    print(get_order_of_point(p0))
