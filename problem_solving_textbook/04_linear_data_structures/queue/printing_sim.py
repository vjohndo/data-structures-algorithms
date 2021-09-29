"""
Lessons learnt: is evaluates if the two objects are pointing to to the same object
    e.g. [1] == [1] is true, [1] is [1] is false

You have a printer and can adjust the print rate. Given a number of students and thier print tasks, what should that speed be?
    >Maths for printer
        * 10 students with 2 print jobs each hour 20 tasks / hour --> 1 task / 180 seconds
        * print jobs range from 1 to 20 pages, inclusive.

    > We will create a queue, and for each second see of a new print task
    > We will also need a printer object and a task object

"""

from pythonds3.basic import Queue
import random

class Printer():
    """
    will need to track if it's working on a task
    how much time needed to complete the task based on pages
    a tick decrements the internal timer
    """
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0
    
    """
    decrements (reduces) the internal timer if it's working on something... remember that the time remining will be calced on a given task
    if the time remaining is 0, we've completed the task and can remove it
    """
    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None 

    """
    Allows the printer queue to check if the printer is not busy and can dequeue a task into the printer 
    """
    def busy(self):
        return self.current_task is not None

    """
    Will have a printer queue popped into this function.
    Will need to a have a task method to get pages 
    """
    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate

"""
A class will be randomly generated 
we will use the rand range function from random to figure this out 
"""
class Task():
    # when the task is created, it will have some time and have a certain amount of pages
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
    
    def get_stamp(self):
        return self.timestamp
    
    def get_pages(self):
        return self.pages
    
    """
    How does this tie in with the printer
    """
    def wait_time(self,current_time):
        # the total wait time of task will be calculated when the printer is finisehd the job
        return current_time - self.timestamp


"""
We now have a queue and a printer and class for queues, let's make this simulation
"""
# Remember how we calculated that for every 180 seconds there would be a new task,
# This is how we would implement it. 
def new_print_task(num_students):
    num_tasks_per_hour = num_students*2
    secs_per_task = int((num_tasks_per_hour/60/60)**-1)
    secs_per_task_inclusive = secs_per_task + 1
    num = random.randrange(1, secs_per_task_inclusive)
    return num == secs_per_task

def simulation(num_seconds, pages_per_minute, num_students):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    # let's tick down some seconds 
    for current_second in range(num_seconds):
        # The helper function goes off and potentially a new task is required
        if new_print_task(num_students):
            task = Task(current_second)
            print_queue.enqueue(task)
        
        # We will also check if the printer is busy and the queue is not empty,
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            # We will the task out of the queue
            next_task = print_queue.dequeue()
            # We will track the time this task has spent in the queue
            # I.e. use the tasks classes method for wait time which captures the current time and minuses the time of init
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)
        
        # lab printer will tick for one second, during which it will reduce the time remaining by 1 second
        lab_printer.tick()
    
    # At the end of the simulation let's calculate the average wait times and the number of tasks remaining
    average_wait = sum(waiting_times)/len(waiting_times)
    print(f" Average Wait {average_wait:6.2f} secs", f"{print_queue.size():3d} tasks remaining. ")

for i in range(10):
    simulation(3600,5,5)


