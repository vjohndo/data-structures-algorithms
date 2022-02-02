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