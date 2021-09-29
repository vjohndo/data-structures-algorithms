"""
- We can use lists to implement a stack in python
- Only thing we need to decide is which end will be considered the top of the stack.
- Let's implement out stack where the "top" is the end of the list, we can utilise methods such as append and pop with are O(n)

Lessons Learned: to run something in the command line 'from module import method'

"""

class Stack:

    # constructor contains a internal data structure of list, containing items 
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def main():
    s = Stack()
    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())

# main()

"""
Write a function that uses a stack to reverse the characters in a string 
"""

def revstring(mystr):
    stck = Stack()
    for char in mystr:
        stck.push(char)
    
    revstr = ""
    while not stck.isEmpty():
        revstr += stck.pop()
    
    return revstr

def test():
    print(revstring('Marshmellow'))
    print(revstring('Watermelon'))

test()