class Signature:
    def __init__(self, r, s):
        self.r = r
        self.s = s

    def __repr__(self) -> str:
        return f'Signature({self.r:x},{self.s:x})'
