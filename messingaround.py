from FieldElement import FieldElement
from Point import Point
from exercises_and_testing import ecc_c3
# from S256Point import S256Point
from S256Point import G
from S256Point import N
from S256Field import S256Field

a = 0
b = 7
p = 223

x1 = FieldElement(192, p)
y1 = FieldElement(105, p)
a = FieldElement(a, p)
b = FieldElement(b, p)

# # s = FieldElement(3, p) * (x1**2) / (FieldElement(2, p) * y1)
# rhs = FieldElement(90, p)**3 + FieldElement(7, p)
# lhs = FieldElement(70, p)**2
# pass
 
# scalar multiplication
# p1 = Point(x1, y1, a, b)
# print(p1)
# print(p1 + p1)
# print(2 * p1)
# print(p1+p1+p1)
# print(3 * p1)

# check if secp256k1 generator point on bitcoin's elliptic curve
gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141 #order
p = 2**256 - 2**32 - 977
a = FieldElement(0, p)
b = FieldElement(7, p)
print(ecc_c3.exercise_1_on_curve(gx, gy, p))

generator_point = Point(FieldElement(gx, p), FieldElement(gy, p), a, b)
print(n * generator_point)

print(N*G)

