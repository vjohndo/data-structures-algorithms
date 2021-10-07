from pythonds3.trees import BinaryHeap

my_heap = BinaryHeap()
my_heap.insert(5)
my_heap.insert(7)
my_heap.insert(3)
my_heap.insert(11)

# Notice that regardless of our order of insertion, we always pull out the the smalled value in this binary heap
print(my_heap.delete())
print(my_heap.delete())
print(my_heap.delete())
print(my_heap.delete())

