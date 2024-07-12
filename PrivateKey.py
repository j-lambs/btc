from S256Point import G, N
from random import randint
import Signature

class PrivateKey:
    def __init__(self, secret):
        self.secret = secret
        self.point = secret * G
    
    def hex(self):
        return f'{self.secret:x}'.zfill(64)
    
    def sign(self, z):
        k = randint(0, N)
        r = (k*G).x.num
        k_inv = pow(k, N-2, N)
        s = (z + r*self.secret) * k_inv % N
        if s > N/2:
            s = N - s
        return Signature(r, s)
    