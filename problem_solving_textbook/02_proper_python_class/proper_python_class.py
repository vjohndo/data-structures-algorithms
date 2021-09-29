import random

class MSDie:
    # Use doc strings to provide some documentation
    """
    Multi-sided die

    Instance Variables:
        current_value
        num_sides

    """
    # construct die, taking number of sides and current value
    # current value will be claculated by rolling the dice
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1,self.num_sides+1) #return from (this number, upto this number)
        return self.current_value
    
    def __str__(self):
        return str(self.current_value)
    
    def __repr__(self):
        return f"MSDie({self.num_sides}) : {self.current_value}"
    
    def __eq__(self,other):
        return self.current_value == other.current_value
    
    def __lt__(self,other):
        return self.current_value < other.current_value


my_die = MSDie(6)
for i in range(5):
    # will need to implement __str__ for this to work
    print(my_die, my_die.current_value)
    my_die.roll()

# will need to implement __repr__ for this to work
d_list = [MSDie(6),MSDie(20)]
print(d_list)

d20 = MSDie(20)
d202 = MSDie(20)

print(d20,d202)
print(d20 > d202)
print(d20 == d202)