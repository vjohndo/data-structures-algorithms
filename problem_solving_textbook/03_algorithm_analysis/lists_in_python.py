"""
Learning about how python implements lists and it's methods / operations

Lessons Learned:
    timeit to create a Timer fir developers to test timing measurements ('statement to time','statement run to set up test')
    timeit operates within it's own namespace
    "__name__" is a built-in dunder method that evaluates the name of the module, if the module is being run directly via the cmdline, it will set this equal to string to "__main__"
    therefore somethign like "from __main__ import test1" would take the module being run and import the test1 function
    timeit vairable "number" defines the number of executions

"""

from timeit import Timer

# for loop, with concatenation
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

# for loop, with append
def test2():
    l = []
    for i in range(1000):
        l.append(i)

# list comprehension
def test3():
    l = [i for i in range(1000)]

# range function wrapped by a call to the list constructor
def test4():
    l = list(range(1000))


# Let's use the timeit to create Timer 
t1 = Timer("test1()","from __main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000),"milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "milliseconds")

# Example output, list(range()) is FASTEST in, "comprehension" 
# Note that these results are the test time, there is some overhead for tunning Timer (could run a blank timer and subtract)
"""
concat  1.1154479009999998 milliseconds
append  0.07701181199999985 milliseconds
comprehension  0.047271300000000016 milliseconds
comprehension  0.02071878599999999 milliseconds

"""


# Let's compare the pop, will the .pop() stay constant?
# in the Timer namespace, import x from main and run a timer on these functions
popzero = Timer("x.pop(0)", "from __main__ import x")
popend = Timer("x.pop()", "from __main__ import x")


"""
This code can't run for more than n number of tests, you'll run out of things to pop.
"""
x = list(range(200000))
print('Popped at zero index',popzero.timeit(number=1000))

x = list(range(200000))
print('Popped at last index',popend.timeit(number=1000))

# but how do make an assessment on it's performance as n increases?

print("pop(0) pop()")
for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    pt = popend.timeit(number=10000)
    x = list(range(i))
    pz = popzero.timeit(number=10000)
    print("%15.5f, %15.5f"%(pz,pt))



