# Python

## Python is an interpreted language
* Python is interpreted
* Python is executed via a Python interpreter
* Programmer writes commands in a *source code* or *script* i.e. the .py files

## Objects in Python
* An assignment statement is something like:
    * my_variable = 120.5

* my_variable is the *identifier*
* 120.5 is the object associated, in this case, a floating point 
* an *alias* is another identifier for an object. Reassignment may break the alias
* evaluating an expression like 98 + 8.0 instantiates a new float object
* *instantiation* invokes the *constructor* of a class
* temp = 98.6 creates an instance of the float class. This expression is known as a literal form.
* a class may define *methods* or *memeber functions* which are invoked on a specific instance of a class using dot notation, e.g. data.sort()
* *accessor* methods do not change the state
* *mutators* or *update methods* can change the state

## Some inbuilt classes
* list - stores sequence of references []
* tuple - immutable list (). If a tuple of length 1, (1,) need to include a comma for python
* str - immutable ' ', escape characters ' \' '
* set - { }
* dict - {key: value}

## Logical operators
* *and* and *or* short circuit

## Equality operators
* *is* for same objects
* *==* for general equivalance. i.e. if same object and if values deemed to be equivalent

## Extended Assignment
* example +=
* if immutable will reassign the identifier to newly constructed variable e.g. string
* lists however redefine the semantics e.g. beta += [4,5] will mutate the original list object. beta = beta + [4,5] will reassign beta to a newly constructed list

## Chaining assigment and comparison
* x = y = 0 
* 1 <= x + y <= 10 is determined as (1 <= x + y) and (x + y <= 10) but x + y is not computed twice

## Conditionals for control flow
* can evaluate nonboolean types as booleans e.g. if somestring: is similar to if somestring != ''

## Break and continue statements 
* continue --> skips this current iteration
* break --> 

## Functions
* Functions are stateless, invoked without the context of a class or some instance
* Methods are invoked with the context of a class

# Activation records
* When a function is called, Python creaste an activation record storing all information relevant to the current call
* namespace of the activation record manages all identifiers that have local scope in the current call
* local scope of function caller has not relationship to any identifier in the caller's scope

# Information passing in functions
* formal parameters --> identifiers for expected parameters 
* actual parameters --> objects sent by caller when invoking the function
* when passing in actual parameters, aliases are made with the formal paramaters for the respective actual parameters 
 
# Default parameters
* functions can support more than one calling signature --> polymorphic
* it is illegal to define something like bar(a, b=15, c)
* if a default parameter is present for one parameter it must be present for all subsequent parameters

# Keyword parameters
* Python allows you explicitly assign an actual parameter to a formal parameter by name
* e.g. foo(c=5)
* this is in contrast to the positional arguments we're familiar with

# Catching an exception
* look before you leap --> use control flow to get rid of exceptions first
* try-except --> try first then run except code on exceptions
* except IOError as e: --> e will be the instance of the exception 
* can use tuples to catch multiple errors e.g. except (ValueError, EOFError):
* error raised in the try: block will skip immediately to the except block
* can have multple except clauses ... much like elif statements  
* can reraise errors by having a single *raise* in the except block
* avoid using except on its own. Difficult to handle and unkown error type
* finally will already run even for uncaught or re-raised exception errors

# Iterators 
* iterator --> object that manges iteration. uses a series of values. has built in function next(iterator_instance)
* iterable --> an object that can produce an iterator. Does this by invoking iter(obj). 
* iterators typically don't store the original collection, instead maintain an indirect reference e.g. the index
* range generates values only one as a time as needed
* can cast a list on to an iterator to get all the values out

# Generators
* Create iterators 
* use of yield 

# Conditional expressions
* expr1 if condition else expr2
* equivalent to the ternerary operator

# Comprehension syntax
* [ expression for value in iterable if condition ]
* set, dictionary, generator compression exist
* { k : k*k for k in range(1, n+1)}
* useful to avoid storing something in memory

# Packing and unpacking sequences
* data = 2, 4, 6, 8 will be treated as a an assignment of a tuple
* unpacking a, b, c, d = range(7, 11)

# similtaneous assigments
* i, j = k, i

# Scopes and namespaces
* global scope 
* local scope 
* each scope has its own namespace 
* python searches through namespaces for each one in order of locality to ifnd the correct one

# First-class objects
* defining a function introduces an identifier in the namespace
* same with classes 

# Modules and importing
* when importing a module top-level commands are executed when the module is first imported
* to deal with this 
* if __name__ == '__main__'