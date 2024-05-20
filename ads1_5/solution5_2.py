''' Lesson 5 task 2 solution. '''

from solution5_1 import Queue

def rotate_queue(queue : Queue, times : int) -> None:
    ''' Rotates queue given number of times (first element becomes last). '''
    if queue.size() == 0 or times <= 0:
        return
    for _ in range(times):
        queue.enqueue(queue.dequeue())
