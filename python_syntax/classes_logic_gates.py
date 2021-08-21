# Lessons learned: classes to extend code
# IS-A, HAS-A relationships

# Logic gate is the most general implementation of the class
# We can eventually build out sub classes from this super class
class LogicGate:

    def __init__(self,n): # Define a constructor method
        self.label = n # Every logic gate will have a label and an ouput
        self.output = None # for the time being we can set the output equal to none & commpute it later

    def getLabel(self): # Method to allow the user to access the label
        return self.label

    # Want to ensure that we can always extend a hierarchy
    def getOutput(self): # Method to allow the user to access the ouput
        self.output = self.performGateLogic() # We don't implement the method yet --> each gate should perform its own logic operation
        return self.output

# Let's create our first subclass, it takes the LogicGate class as an input
class BinaryGate(LogicGate):

    def __init__(self,n): # Define our constructor 
        
        # We want to start with what's already built in the logic gate
        LogicGate.__init__(self,n) # Notice how the parameters for the Binary __init__ is the same the Logic Gate __init__
        # and Binary gates have two inputs, in computer circuit design, these are called pins
        # we will add these data objects to the binary subclass
        self.pinA = None
        self.pinB = None
    
    # It would be nice to be able to define the inputs for those pins
    ## BACK FROM THE FUTURE... we've built a connector, meaning that if we want to access a pin it may already be connected
    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+" --> "))
        else:
            return self.pinA.getFrom().getOutput() #self.pinB will be a connector object
                                                    #getFrom is a connector method, gives you "from" logic gate. form the "from" logic gate object, you will call "getOutput"

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+" --> "))
        else:
            return self.pinB.getFrom().getOutput() #self.pinB will be a connector object
                                                    #getFrom is a connector method, gives you "from" logic gate. form the "from" logic gate object, you will call "getOutput"

    ## CODE FROM THE FUTURE
    # We have to implement gate at this level of heirarchy as the inputs are same 
    # Consider a binary gate, with 2 possible imputs, connector must connect to one line only
    # start with A by defailt, then go for B, otherwise there are no available inputs
    # This function will take in the source pin
    # note that the getPin methods which were based on human (external) input now need to be editted 
    def setNextPin(self, source): # source parameter is the connect object.
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
        super(UnaryGate,self).__init__(n) #Super function can be useful instead of explicity naming the parent class 
        self.pin = None
    
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+" --> "))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
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


# A NandGate is effectively an AndGate with a not at the end of it
class NandGate(AndGate):

    # Note that we do not have to initialise, we can just OVERWRITE the perform gate logic
    # Let's call the parent method... we could calll AndGate.performGateLogic or...
    # 
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

class NorGate(OrGate):
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


# HAS-A relationship, the connector HAS instances of Logic gate class
class Connector:
    # define the constructor and build the from gate and the to gate
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        # we will need to define a method to EACH OF OUR CLASSES to set next pin for the "togate"
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

def test():
    g1 = NorGate("G1")
    g2 = NandGate("G2")
    c1 = Connector(g1,g2)
    print(g2.getOutput())

test()
