# 2 questions: how to implement a stack with 2 queues, and how to implement a queue with 2 stacks.
from collections import deque as queue

# A stack from 2 queues.
class StackByQueues():
    def __init__(self):
        self.q1, self.q2 = queue(), queue()
        self.size = 0
    
    def push(self, v):
        self.q1.appendleft(v)
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            raise IndexError("pop from empty stack")
        for _ in range(self.size - 1):
            self.q2.appendleft(self.q1.pop())
        v = self.q1.pop()
        self.size -= 1
        self.q1, self.q2 = self.q2, self.q1
        return v

class QueueByStacks():
    def __init__(self):
        self.s1, self.s2 = [], []
        self.size = 0
    
    def enqueue(self, v):
        self.s1.append(v)
        self.size += 1
    
    def dequeue(self):
        if self.size == 0:
            raise IndexError("dequeue from empty queue")
        
        for _ in range(self.size - 1):
            self.s2.append(self.s1.pop())
        v = self.s1.pop()
        self.size -= 1

        for _ in range(self.size):
            self.s1.append(self.s2.pop())
        return v