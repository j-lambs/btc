from FieldElement import FieldElement
from Point import Point

a = 0
b = 7
p = 223

x1 = FieldElement(192, p)
y1 = FieldElement(105, p)

# s = FieldElement(3, p) * (x1**2) / (FieldElement(2, p) * y1)
rhs = FieldElement(90, p)**3 + FieldElement(7, p)
lhs = FieldElement(70, p)**2
pass

