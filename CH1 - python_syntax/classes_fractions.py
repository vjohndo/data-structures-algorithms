# We will need to define a helper function for LCD
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


def intToFraction(intVar):
    return Fraction(intVar,1)

# A fraction class
class Fraction:

    # constructor method
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    # show method to help with outputing the object
    def show(self):
        print(self.num,"/",self.den)

    # __str__ is method for converting object to string
    # we will need to overwrite it 
    def __str__(self):
        return (f"{self.num}/{self.den}")

    # __add__ operand '+' doesn't know what to do with our fraction
    def __add__(self,other):
        if isinstance(other,int):
            other = intToFraction(other)
        newNum = self.num*other.den + self.den*other.num
        newDen = self.den * other.den
        common = gcd(newNum,newDen)
        return Fraction(newNum//common,newDen//common)

    def __eq__(self,other):
        if isinstance(other,int):
            other = intToFraction(other)
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __sub__(self,other):
        if isinstance(other,int):
            other = intToFraction(other)
        newNum = self.num*other.den - self.den*other.num
        newDen = self.den * other.den
        common = gcd(newNum,newDen)
        return Fraction(newNum//common,newDen//common)

    def __mul__(self,other):
        if isinstance(other,int):
            other = intToFraction(other)
        newNum = self.num * other.num
        newDen = self.den * other.den
        common = gcd(newNum,newDen)
        return Fraction(newNum//common,newDen//common)

    def __lt__(self,other):
        if isinstance(other,int):
            other = intToFraction(other)
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    def __gt__(self,other):
        if isinstance(other,int):
            other = intToFraction(other)
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum


my_fraction = Fraction(2,4)
my_fraction2 = Fraction(6,12) + 77
my_fraction3 = Fraction(1,4) 
print(my_fraction2)

print(my_fraction == my_fraction2)

print(my_fraction2-my_fraction3)

new_fraction = my_fraction < my_fraction2
print(new_fraction)