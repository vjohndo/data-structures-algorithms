*** Notes I had on google doc from almost

coding practice websites:
Basic Practice:
http://codingbat.com/python
More Mathematical (and Harder) Practice:
https://projecteuler.net/archives
List of Practice Problems:
http://www.codeabbey.com/index/task_list
A SubReddit Devoted to Daily Practice Problems:
https://www.reddit.com/r/dailyprogrammer
A very tricky website with very few hints and touch problems (Not for beginners but still interesting)
http://www.pythonchallenge.com/

// 


7/11/2020, 8/11/2020
Sections 1 & 2
Learned cmd commands
cd - current directory 
dir
cd ..
press tab to complete item
“” around items with space to make it one object
cls
python(‘’)
quit
Environments are what you type python code into
Learned python code
print
Sublime text editor 
Jupyter notebook
shift+enter to run a cell
markdown = notes

Section 3: Python object and data structure basics
Learned these functions
type() tells you the data type 
len() tells you the length of the string
sorted() pass through the list to be sorted 
pressing tab after variable. returns a list of attributes / methods available for the string object
x.upper() > makes it upper case 
x.lower() makes everything lowercase
x.split() splits a string based on space or letter you pass in, remember that this accepts strings only
Learned these commands
% : mod - returns remainder after division
can check if divisible, even, odd, 
** : to the power
// : this is floor division, truncates the decimal with no rounding
Python lets you add, subtract, multiply and divide numbers with reassignment using +=, -=, *=, and /=. (adding a space after the function) 
a = a + 2 is the same as a+=2
Variables
keep them lowercase
avoid words that have special meaning 
Python uses dynamic typing; okay to assign different data type 
restart the kernel to delete all variables
Strings	“”
strings can be concatenated e.g. ‘String 1’ + ‘String 2’ or ‘String 1’*10
can be single quote and double quotes
ordered, can index and slice
index can be reversed i.e. -1 is the last number 
slicing notation [start:stop, but not including:step]
“ vs ‘ to help python identify which one 
print: (make sure the following are backslashes)
\n is an escape character, treat it as a new line 
\t is an escape character for tab
len(): tells you the length of a string
String indexing and string slicing
indexing notation [start:stop:step], starts at 0
[start:] = all the way to the end
stop goes up to be but not including 
[] = zero index
space counts as a character
step size = jumps
-1 for step allows you reverse 

immutability - can’t be mutated, can’t change what’s in a string 
need to create a new string and can use + - / * etc.
watch out as data as a string will be concatenated rather than mathed.
interpolation - injecting variables into strings for printing
Interpolation - sticking a variable into a string
% placeholders 
%s in the string so that %(‘xxx’,’xxx”) gets inserted
Very similar to above
%r delivers the string representation
%d delivers the string after rounding rounding the number to an integer 
%x,xf for setting the precision of strings from floating point
can include multiple conversion types (“tshis”,321)
.format()
.format(‘string1’,’string2’) fills in the {}
can index using the {2} etc. 
can assign keywords instead of indexing, almost like a variable assignment (f=”fox”) which would sub into {}
Can add precision
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))
Left     |  Center  |    Right
11       |    22    |       33
{value:width.percision f} for floating
f-strings (formatted string literals)
allows you skip the formatting
print(f’string {variable_name}’)
{xxx!r} will deliver it as the string representation
num:{padding}.{rounding to SF}
f literals can’t pad to the right … i.e. 3.00000
num:{10}.{6} vs {num:10.4f}
Preferred method
f-string literals with .format() syntax for padding. 
lists []
New functions
listvariable. #then you can look at the different options 
.append allows you add another item to the end of the list 
.pop, pops off and returns the last entry
Can pass the index number through pop
reverse indexing works
e.g. pop(0) pops the first item in the list 
.sort - but this occurs in place, can’t pass it through other items 
.extend - continues a list with new list input; very useful as using append will nest the list
can concatenate + or * 
can index like a string 
can slice like a string 
importantly, lists can be mutated i.e. mutable
dictionaries {}
unordered, unsorted, mapping to store objects
can’t index / slice
key value pair 
{‘string key’:item}
call the item back using [‘key2’]
can hold lists, even other dictionaries
can call for [] items on the same line.
in - d = {'key':['a','b','c']}
out - d['key'][2].upper()
return = 'C'
to add a new item, call up a new string and assign it the pair
.keys(), returns back all the keys
.values(), returns back all the values 
.items(), returns back all the pairings
when using these and printing with a string, make sure to use a different set of “”
tuples(,,)
immutable strings
similar, can check the length 
can take on multiple object types
.count(‘item’) counts the number of times ‘items’ appears in the code
.index(‘item’) returns back the first time the index appears 
provides data integrity
can unpack a tuple like so:
x,y = tuple
set(,,,,) = {}
unordered UNIQUE elements
unordered means that if you compare two sets, that look like they have different order. they’ll still be the same 
.add(1) added whatever (must be assigned for this to work)
useful to cast a list to set to only get the unique values 
set(list)
an empty set will look like this ()


booleans 
True/False
watch out for capitalisation in Python
None
input and output with basic text files
jupyter notebook and file should be saved in same directory
pwd - print working directory, where your notebook is currently working
methods
.read() - note this moves the cursor to the end of the file 
.seek(0) - moves the cursor back to zero
.readlines() - this give the lines
.write() - duhh
folder paths use double backslash to not mix up the 
need to close it, cause python is closing
with open('myfile.txt') as my_new_file:
any variable in the indent will have open(‘myfile.txt’) as my_new_file
open 
reading and writing to basic text file
on Jupyter can click shift+tab next to open to browse through the existing functions
helps you get further information about the function
mode = ‘r’ , is read
mode = ‘w’, is write (potentially overwriting files)
mode = ‘a’, is append 
mode = ‘r+’ reading and writing
mode = ‘w+’ writing and reading (overwrites existing or creates a new file)
Section 4:
Comparison operators
the constant equal is always to the right
Logical operators
and
or
not - returns the opposite boolean

Section 5: 
Control flow 
Nested if statements probably means you could’ve thrown a logical operator in there 
If condition:
run code
elif:
else:
For loops
for *variable name for each item* in *list/string/tuple etc. - iterable object*
run this code
tuple unpacking: tuples inside a list
mylist = [(1,2),(3,4),(5,6),(7,8)]
for (a,b) in mylist:
    print(a)
    print(b)
d = {'k1':1,'k2':2,'k3':3}
for item in d, only runs through the keys   
need to for _ in d.items():
can use in conjunction with else:
if i went through this entire for loop and it never executed run this code
checks to see if you’ve ever broken out of the above for loop
If you have run the code below


While continue to executes code until a while code 
while some condition persists
consider the fact the condition can change too
can combine the while loop with “else”
break, continue, pass
breaks out of the closest enclosing loops ← very important for while loops 
continue to the top of the closes enclosing loop (skip everything below and run the loop) 
pass do nothing at all (good place holder for 
useful operators
RANGE:
range(), returns number from 0 up to including the number passed
i.e. not inclusive of the high 
range(start,stop,step)
range is a generator, would need to cast it to a list to use it on its own
list(range())
more efficient to generate a list rather than storing a set of numbers
ENUMERATE.(sequence)
puts item into tuples and allows you to do the index count with one less line
otherwise cast into a list
ZIP
puts all the items back as tuples 
can cast the zip into a list
IN
is it in a sequence
for dictionaries remember that it calls the for the keys first
need to specify if you’re calling out the item
MIN
MAX
import
from “random library” import “this function”
INPUT - will always accept everything as a string though - need to make it a nmumber 
FLOAT
INT
list comprehensions OH BABY
better versions of doing for loops and .append()
mystring = ‘hello’
my_list = [letter for letter in mystring]
current variable is letter being assigned to string and changes depending on letter
letter to be appended coming out of the for loop’s letter
Can then then throw in an if statement at the end to only append on a true state
can add elifs at the the end but the order will be different as you need to start writing the if else before the for
results1 = [x if x%2 == 0 else 'ODD' for x in range(0,11)]
print(results1)


results2 = [x for x in range(0,11) if x%2 == 0]re
print(results2)
can nest loops:
mylist = [] 
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
        
mylist = [x*y for x in range(2,8,2) for y in range(100,400,100) ]



Functions 
def name_of_function(args)
function code
return allows you assign something to a variable
remember a == b will return either true or false
1, 0 correspond to true / false - use it if you’re writing if statements
provide a default arg
def name_of_function(arg = default argument)
return automatically breaks out of the function 
when running a loop to check if something is in a list, make sure to check when to break out an




*args, allows you to make a tuple pass in lots of arguments (args it self is arbitrary)
def myfunc(*args)
it will then be treated as a tuple inside
this is better than trying to assign default variables (a,b,c=0,d=0) etc. 


**kwargs, allows you build dictionaries using keyworded arguments
arguments passed through would be keyword = “value”
allows you take in an arbitrary number of arg/kwargs

first key word in not a string
allows the user to define the parameter and use them later on
can have both *args, **kwargs but inputs need to follow that order 
Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:



How to lean code faster
Comments with my own example 


Lambda expressions, map and filter functions

Lambda - anonymous 1 time functions
start out with a function
run the whole thing on one line

get rid of def, function name, and the return

i.e. lambda input: return 
then assign it to a variable

typically you DON’T assign it, but it’s super handy with map and filter functions
Map function - (func, iterable)
	similar to the enumerate()
allows you make an iterable where a function is applied to each iterable
applies (function, to all these iterables)
Can wrap it back up in a list 
Filter function - 
grabs numbers from an iterable, only given a condition.
filters based off of a functions condition, needs a boolean 
i.e. it maps the function to all the iterables, and then grabs only the booleans that come back true but as the original value


-- Nested statements and scope
scope: rules that define which variables looks for when you call for it 
name spaces: 
Local e.g. inside a lambda function
Enclosed function locals e.g. 
Global (module) e.g. no function level 
Built-in 
so how do you say get the global variable vs local variable:
declare the global space and the variable you want, underneath the function
def func(): --- notice how since we will be taking the global variable, no need to input it to function.
global x 
as a beginner probably want to avoid doing this. and just reassign the variable re


multiplication assignment
if A = 2
A *= 5
now A = 10


Can concatenate strings e.g. [“ “]*10 == [“ “, “ “, … etc]
Tuple unpacking
	varA, varB = (1,0)
now
	varA = 1
	varB = 0



remember to be efficient with returns 

OOP:
allows users to make objects with their own attributes / methods
allows us to create repeatable and organised code
especially helpful when using outside libraries

-- 
class Dog():
	# Class object attribute
	species = ‘Mammal’
	
	# define class instance attributes
	def __init__(self)
	self.breed
	
	# Method i.e. function on the class instance
	def bard(


an object.attributes/methods 
these are types of object e.g. a list, set etc. 
OOP allows 
class is a blueprint for future user created objects 
can then create instances of the class


--
How do we now create attributes for these classes 
Classes use Camel typing 

__init__ → constructor for our class, will be called automatically when you call for an instance
self → represents instance of the object itself 
after that need to define the attributes for the instance of the class
attributes of the said class instance do not have to be a string, e.g. can be a bool/string CAN BE DEFINED BY EQN e.g.
	self.radius = radius
	self.area = radius*self*pi()*2

watch out for type control tho
--
Can define a class object attribute, these are the same for any class
can reference as either self.attribute / ClassName.attribute
--
# more l
methods = functions acting on the class instance self - typically using the information 
notice that attributes, no parenthesis as there’s nothing to execute.
methods have parenthesis

whenever you’re calling for a variable in method, you need to reference the particular instance 
this includes the class object attributes
--
methods can take in outside arguments 
    def bark(self,number):
        print("WOOF! My name is {} and the number is {}".format(self.name,number))

call the above will get an error if you don’t call in args will expect 1 argument ‘number’

--
Just like in functions you can define a default value 
e.g. def __init__(self, radius = 1) 

--
can reference class objects like this → Class.attribute

Inheritance and Polymorphism
Inheritance, form new classes using old classes 
To do so pass in the old class e.g. class Dog(Animal): 
and call the passed in __init__ function
This allows you to use the methods in the base class
Can still add more
- 
Polymorphism - 
Different object classes can share the same name but with different purposes
You can use that to your advantage e.g. in for loops or pass it into a function to call that method 
Abstract classes - only serves as a base class for inherited class 
once you create subclasses, you can overwrite the methods 

Special Methods:
Built in operations with our own user created ones 
e.g. how can you print / len your OOP
dunder or magic methods dunder = double underscore 
def __str__ (self):
return some string thing
def __len__ (
del → used to the delete variable from memory, can add extra things thanks to class
e.g. 
def __del__(self):
print(‘This has been deleted’)

Upacking
x,y = tuple


Modules and Packages → How to organis .py scripts 
PyPI - open source libraries 
pip install installs these external packages
pip has already been installed 
steps:
pip install
from library import init
init()
from library import 
Writing your own modulus and packages:
Module → just a .py script, to be used in another script
Package → collection of modules 
To create a package, use the the file structure Camel Casing
Then in each file, enter in the __init__
To call upon the package
from package.subfolder import script
then to call a function from the script
script.functiontobecalled 
if __name__ == “__main__”
you want to know if the module is an import
or if you’re using an original .py file of that module 

Section 10: Errors and exceptions handling
Error in the program will stop the entire program
We want to try and let the other code run and possibly report the error as well
Keywords:
try - try the code, 
except (can specify specific errors) - if there is an error, run this code 
else - if there’s no error run this 
finally - will always run this code 
Unit testing - you’ll need to have tests in place so that previous code still runs as expected
pylint: looks at code and reports issues
at the command line, run pylint script.py
unittest: built in
useful to help you check that you’re still getting expect values as other people may be trying to access 
--
unittest allows you to write your own test 
it sends data to your program and checks if you get the expected result 
you do build out a test class. 
--
need to create a test.py file
create  class that inherits the TestCase class 
generally run from simple to complex 
Example:
	def test_multiple_words(self):
		text = 'monty python'
		result = cap.cap_text(text)
		self.assertEqual(result,'Monty Python')


Truthyness

zero =  0 → False
one = 1 → True
two = 2 → True

ie. 
if two = if True

> ace counter would be less computational
> try, except and finally would have been handy 
> could have used more functions in order to make code more readable 

---
decorators
you can define a function in a funcion
you can then assign one of those nested functions to a variable
variable = function_returned_from_another_function
you can then call on that function e.g. function_returned_from_another_function()
you can pass that function in another function
notice that the function has no (), meaning it is not being executed
This is just the function as an object 

def new_decorator(original_func):
    
    # wrap func is the extra functionality you want to decorate the original functino with
    def wrap_func():
        print('Some extra code, before the original function')
        
        original_func()
        
        print('Some extra code, after the original function!')
        
    return wrap_func


---
generators:
> this is good if you’re iterating through a bunch of numbers and storing it in lists
You can define a value and pick it back up from where it left off
this requires the use of ‘Yielding’
It’s more better this way than to create some huge list in memory 
# let's start by creating a basic function
def create_cubes(n):
for x in range(n):
      # instead of returning some result we will yield
      # what we want returned
      yield (x**3)

generator functions are built on the:
next function: remembers what the last yielded is and goes to next one
you’ll eventually run into an iteration error
note that for loops naturally catch this
a for loop is effectively a series of next functions 
iter function 
iter function turns objects you usually can’t iterate over into an iterator
e.g. next(‘string’) doesn’t work
you need to iter(‘string’)

Section 14: Advanced Python Modules
Collections:
Counter, counts unique elements in a list
has a most common method which is pretty handy 
can cast it into a list
defaultdict
calling a wrong key in a normal dict, it’ll return an error
it will assign a default value if a key fault error occurs
deafaultdict(lambda: 0)
namedtuple
sort of like a class
get’s rid of the issue of not remembering the index 
