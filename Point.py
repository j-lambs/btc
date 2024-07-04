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
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError('({}, {}) is not on the curve'.format(x, y))
        
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
        if self.x != None and self.y != None:
            return f'Point({self.x}, {self.y})_{self.a}_{self.b}'
        return 'Point(infinity)'
    
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

        # x1 = x2
        if self == other:
            # Case: tangent is vertical
            if self.y == 0:
                return self.__class__(None, None, self.a, self.b)
            slope = (other.y - self.y) / (other.x - self.x)
            x3 = slope**2 - (2 * self.x)
            y3 = slope * (self.x - x3) - self.y
            return self.__class__(x3, y3, self.a, self.b)
