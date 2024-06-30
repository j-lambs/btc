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

    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not (self == other)
