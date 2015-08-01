""" queue.py: Implementation of queue abstract data structure. """

__credit__ = "CLRS"

class Queue:
    def __init__(self, allocation = None):
        self.size = allocation or 50
        self.buffer = [None]*self.size
        self.head = 0
        self.tail = 0
        
    def _inc(self, i):
        if i < self.size-1:
            return i+1
        else:
            return 0
            
    def _isEmpty(self):
        """ Returns True if there is an empty space in the buffer. """
        return (self.head == self.tail)
        
    def _isFull(self):
        """ Returns True if there is no empty space in the buffer. """
        return (self._inc(self.tail) == self.head)
            
    def enqueue(self, x):
        """ Adds an element to the queue. """
        if self._isFull():
            raise ValueError("No space left in the queue.")
        else:
            self.buffer[self.tail] = x
            self.tail = self._inc(self.tail)
            
    def dequeue(self):
        """ Removes the first added element from the queue. """
        if self._isEmpty():
            raise ValueError("No elements in the queue.")
        else:
            index = self.head
            self.head = self._inc(self.head)
            return self.buffer[index]
            
