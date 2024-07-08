from FieldElement import FieldElement
from Point import Point

P = 2**256 - 2**32 - 977

class S256Field(FieldElement):
    """
    """
    def __init__(self, num, prime=None):
        super().__init__(num, prime)
    def __repr__(self):
        return '{:x}'.format(self.num).zfill(64)