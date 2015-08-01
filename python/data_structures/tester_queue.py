""" tester_queue.py:
        Implements unit tests for queue.py. """
        
import unittest
from random import randrange

from queue import Queue

class QueueTester(unittest.TestCase):
    def setUp(self):
        self.Q = Queue(25)

    def test_increment(self):
        """ Testing queue index incrementing. """
        for _ in range(10):
            __ = randrange(24)
            self.assertEqual(__+1, self.Q._inc(__))
        self.assertEqual(0, self.Q._inc(24))

    def test_isEmpty_truth(self):
        self.assertTrue(self.Q._isEmpty())
    
    def test_isEmpty_false(self):
        self.Q.enqueue(1)
        self.assertFalse(self.Q._isEmpty())
        
    def test_isFull_truth(self):
        for _ in range(25):
            self.Q.enqueue(_)
        self.assertTrue(self.Q._isFull())
    
    def test_isFull_false(self):
        self.assertFalse(self.Q._isFull())

    def test_enqueue_success(self):
        for _ in range(20):
            __ = randrange(100)
            self.Q.enqueue(__)
            self.assertEqual(self.Q.buffer[self.Q.head], __) ## !!!
            self.assertEqual(self.Q.tail, _+1)
        
    def test_enqueue_failure(self):
        for _ in range(25):
            self.Q.enqueue(_)
        with self.assertRaises(ValueError):
            self.Q.enqueue(-1)
    
    def test_dequeue_success(self):
        _ = randrange(50)
        self.Q.enqueue(_)
        self.assertEqual(self.Q.dequeue(), _)
        
    def test_dequeue_failure(self):
        with self.assertRaises(ValueError):
            self.Q.dequeue()
            
if __name__ == "__main__":
    unittest.main()