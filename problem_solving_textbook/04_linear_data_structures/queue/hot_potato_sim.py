"""
For each turn, the front of the queue is popped and and immediately enqeueud
However after x number of turns, that popped person is removed form the game instead of being enqueued 
"""

from pythonds3.basic import Queue

def hot_potato(name_list, num):
    
    # Create an instance of the queue and add everyone to the queue
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        # run the number of steps
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        
        sim_queue.dequeue()
    
    return sim_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))