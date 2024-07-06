from FieldElement import FieldElement

class Point:
    """
    A class for points on a elliptic curve.
    An elliptic curve is defined by the equation y^2 = x^3 + ax + b
    """
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        # x = y = None signifies infinity point
        if self.x is None and self.y is None:
            return
        # check if point is on elliptical curve
        if self.y**2 != self.x**3 + (a * self.x) + self.b:
            raise ValueError(f'({x}, {y}) is not on the curve')
        
    def on_curve(self, x, y):
        """
        Pass an (x,y) ordered pair to this function. It will tell you if it is 
        on the same curve as the curve that defines the point object.
        """
        y_sq = y**2
        x_cubed = x**3
        if y**2 == x**3 + (self.a * x) + self.b:
            return True
        return False

    def __repr__(self) -> str:
        if self.x is None:
            return 'Point(infinity)'
        elif isinstance(self.x, FieldElement):
            return 'Point({},{})_{}_{} FieldElement({})'.format(
                self.x.num, self.y.num, self.a.num, self.b.num, self.x.prime)
        else:
            return 'Point({},{})_{}_{}'.format(self.x, self.y, self.a, self.b)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not (self == other)
    
    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError(f'Points {self}, {other} are not on the same curve')
        # point + (point at inf) = point bc inf is identity
        if self.x is None:
            return other
        if other.x is None:
            return self
        # identity + identity = 0
        if self.x is None and other.x is None:
            return self.__class__(None, None, self.a, self.b)
        
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)
        
        if self.x != other.x:
            slope = (other.y - self.y) / (other.x - self.x)
            x3 = slope**2 - self.x - other.x
            y3 = slope * (self.x - x3) - self.y
            return self.__class__(x3, y3, self.a, self.b)

        if self == other:
            if isinstance(other.x, FieldElement):
                # Case: tangent is vertical
                if self.y.num == 0:
                    return self.__class__(None, None, self.a, self.b)
                else:
                    #TODO: change to derivative eqs
                    slope = (FieldElement(3, self.x.prime) * self.x**2 + self.a) / (FieldElement(2, self.x.prime) / self.y)
                    x3 = slope**2 - (FieldElement(2, self.x.prime) * self.x)
                    y3 = slope * (self.x - x3) - self.y
                    return self.__class__(x3, y3, self.a, self.b)
            # Case: tangent is vertical
            elif self.y == 0:
                return self.__class__(None, None, self.a, self.b)
            slope = (other.y - self.y) / (other.x - self.x)
            x3 = slope**2 - (2 * self.x)
            y3 = slope * (self.x - x3) - self.y
            return self.__class__(x3, y3, self.a, self.b)
