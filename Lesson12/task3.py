def gcd(numerator, denominator):
    while denominator:
        numerator, denominator = denominator, numerator % denominator
    return numerator

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int) and not isinstance(denominator, int):
            raise TypeError("Must be integer")
        if denominator == 0:
            raise ZeroDivisionError("The denominator cann`t be zero")
        self.top = numerator
        self.bottom = denominator

    def __str__(self):
        if self.bottom == 1:
            return self.top
        elif self.top >= self.bottom:
            return f"{self.top//self.bottom} {self.top % self.bottom}/{self.bottom}"
        else:
            return f"{self.top}/{self.bottom}"

    def __add__(self, other):
        newtop = self.top * other.bottom + other.top * self.bottom
        newbottom = self.bottom * other.bottom
        common = gcd(newtop, newbottom)
        return f"{newtop//common}/{newbottom//common}" if abs(newtop//common) != abs(newbottom//common) else (newtop//common)//(newbottom//common)

    def __sub__(self, other):
        newtop = self.top * other.bottom - other.top * self.bottom
        newbottom = self.bottom * other.bottom
        common = gcd(newtop, newbottom)
        return f"{newtop//common}/{newbottom//common}" if abs(newtop//common) != abs(newbottom//common) else (newtop//common)//(newbottom//common)

    def __mul__(self, other):
        return f"{self.top * other.top}/{self.bottom * other.bottom}"

    def __truediv__(self, other):
        return f"{self.top * other.bottom}/{self.bottom * other.top}"


if __name__ == '__main__':
    x = Fraction(1, 3)
    print(x)
    y = Fraction(2, 3)
    print(y)
    print('sum', x + y)
    print('mult', x * y)
    print('sub', x - y)
    print('div', x / y)
