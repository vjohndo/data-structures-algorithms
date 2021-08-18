class LogicGate:
    # Classes are very effective for allowing the construction of sub classes
    # Every logic gate will have a label and an ouput, for the time being we can set the output equal to none
    def __init__(self,n):
        self.label = n
        self.output = None

    # Method to allow the user to access the label
    def getLabel(self):
        return self.label

    # Method to allow the user to access the ouput
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

    # Note how we didn't want include a function to perform the gate logic
    # We don't know how each gate will perform its logic
    # best to be included in the heirarchy, that means

# Let's create our first subclass, it takes the LogicGate class as an input
class BinaryGate(LogicGate):

    # As always we need to build a constructor function
    def __init__(self,n):
        # and we want to start with what's already built in the logic gate
        # Notice how the parameters for the Binary __init__ is the same the Logic Gate __init__
        LogicGate.__init__(self,n)
        # and Binary gates have two inputs, in computer circuit design, these are called pins
        self.pinA = None
        self.pinB = None
    
    # It would be nice to be able to define the inputs for those pins
    def getPinA(self):
        return int(input("Enter Pin A input for gate"+self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate"+self.getLabel()+"-->"))

# Create subclass
class UnaryGate(LogicGate):

    # Create the constructor function, using the super class constructor
    def __init__(self,n):
        #Super function can be useful instead of explicity naming the parent class 
        super(UnaryGate,self).__init__(n)
        self.pin = None
    
    def getPin(self):
        return int(input("Enter Pin B input for gate"+self.getLabel()+"-->"))

# creeating the and gate
class AndGate(BinaryGate):

    def __init__(self,n):
        super(AndGate,self).__init__(n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a==1 and b==1:
            return 1
        else:
            return 0

g1 = AndGate("G1")
print(g1)
    