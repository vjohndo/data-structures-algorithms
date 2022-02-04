OOP Design Goals:
- Robustness --> want the program to be able to be okay if incorrect error
- Adaptability --> want to be able to evolve teh software. Portability --> minimal changes to SW on different HW
- Reusability

OOP Design Principles:
- Modularity --> dividing components of SW into seperate functional units
- Abstraction --> distilling a system to its most fundamental parts. E.g. an ADT specifies type of data stored, operations and parameters on those operations but NOT how.
- Encapsulation --> Components should not reveal internal deatails of thier implementation. Allows you to worry only about the public interface. Limited Python support, assumes that memebers starting with _ is non-public.

Design Patterns:
- Design patterns describes a solution to typical design problem 

Design:
- Responsibilities --> work is done by actors i.e. classes
- Independence --> each class should be as independent as possible i.e. autonomous
- Behaviours --> each class has behaviours i.e. methods and interfacing.
- Defind actions and then determine actors 

Documentaion:
- hashtag for explaining code
- """ for documenting code 

Testing:
- Method coverage (each method is tested)
- Statement coverage (each statement is tested)
- Can us if __name__ = '__main__'

Common special cases:
- 0 length, 1 length
- All same
- Already sorted
- Reverse sorted

Class:
- member function aka methods 
- attributes aka field, instance variables, data members

Self:
- Identifies the instance upon which a method is invoked 
