""" stack.py
        Simple implementation of stacks in Python. 
        
        Really, really simple. Not really worth the effort here. """
        
class Stack:
    def __init__(self):
        self._buffer = []
        
    def isEmpty(self):
        return self._buffer == []
        
    def push(self, x):
        self._buffer.append(x)
        
    def pop(self):
        return self._buffer.pop()
        
    def peek(self):
        return self._buffer[-1]
        
    def size(self):
        return len(self._buffer)
        
    
