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
    ## BACK FROM THE FUTURE... we've built a connector, meaning that if we want to access a pin
    ## it may already be connected
    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate"+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOuput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate"+self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    ## CODE FROM THE FUTURE
    # Consider a binary gate, with 2 possible imputs, connector must connect to one line only
    # start with A by defailt, then go for B, otherwise there are no available inputs
    # This function will take in the source pin
    # note that the getPin functions which were based on human input now need to be editted 
    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

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

class OrGate(BinaryGate):

    def __init__(self,n):
        super(OrGate,self).__init__(n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a==1 or b==1:
            return 1
        else:
            return 0

# Create subclass
class UnaryGate(LogicGate):

    # Create the constructor function, using the super class constructor
    def __init__(self,n):
        #Super function can be useful instead of explicity naming the parent class 
        super(UnaryGate,self).__init__(n)
        self.pin = None
    
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin B input for gate"+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pinA = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


# HAS-A relationship, the connector HAS instances of Logic gate class
class Connector:
    # define the constructor and build the from gate and the to gate
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        # we will need to define a method to set next pin for the "togate"
        # this is the functionality that allows you connect to next gate
        tgate.setNextPin(self)
    
    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())

main()
    