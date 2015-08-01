""" arbitrary_tree.py
        Tests the ArbitraryTree and ArbitraryNode methods. """
        
import unittest

from arbitrary_tree import ArbitraryTree, ArbitraryNode

class TreeTester(unittest.TestCase):
    def setUp(self):
        """ Initialize! 
            T.root
             /
            a -- b """
        self.T = ArbitraryTree(99)
        self.a = ArbitraryNode(1)
        self.b = ArbitraryNode(2)
        
        self.a.parent = self.T.root
        self.b.parent = self.T.root
        self.T.root.child = self.a
        self.a.sibling = self.b
        
    def test_defaultValues(self):
        """ Making sure initial values are initialized properly. """
        self.assertIsNone(self.T.root.sibling)
        self.assertIsNone(self.T.root.parent)
        self.assertIsNone(self.b.sibling)
        self.assertIsNone(self.a.child)
        
    def test_isLeftmostSibling(self):
        """ Checking that we can find a Node's leftmost sibling. """
        self.assertTrue(self.a.isLeftmostSibling())
        self.assertFalse(self.b.isLeftmostSibling())
        
    def test_isLeftmostSibling_integrity(self):
        """ Checking that we CAN find a Node's leftmost sibling. """
        self.assertEqual(self.a, self.a.parent.child)
        self.assertEqual(self.a, self.b.parent.child)
        
    def test_getInitialSibling(self):
        """ Checking that we can get the initial sibling. """
        self.assertEqual(self.b.getInitialSibling(), self.a)
        self.assertEqual(self.a.getInitialSibling(), self.a)
        self.assertEqual(self.T.root.getInitialSibling(), None)
        
    def test_getTerminalSibling(self):
        """ Checking that we can get the terminal sibling. """
        self.assertEqual(self.a.getTerminalSibling(), self.b)
        self.assertEqual(self.b.getTerminalSibling(), self.b)
        self.assertEqual(self.T.root.getTerminalSibling(), self.T.root)
        
    def test_getSiblings(self):
        """ Checking that we can get an array of a Node's siblings. """
        self.assertEqual(self.T.root.getSiblings(), [])
        self.assertEqual(self.a.getSiblings(), self.b.getSiblings())
        self.assertEqual(self.a.getSiblings(), [self.a, self.b])    

    def test_getChildren(self):
        """ Checking that we can get an array of a Node's children. """
        self.assertEqual(self.T.root.getChildren(), [self.a, self.b])
        self.assertEqual(self.a.getChildren(), [])
        
    def test_getTerminalChild(self):
        """ Checking that we can get the terminal child. """
        self.assertEqual(self.T.root.getTerminalChild(), self.b)
        
    def test_killNode(self):
        """ Checking that we can kill a Node. """
        self.b.killNode()
        self.assertIsNone(self.b.parent)
        self.assertIsNone(self.b.child)
        self.assertIsNone(self.b.sibling)
        
    def test_addNode_withSibling(self):
        """ Checking we can add a Node to a parent with children. """
        y = self.T.createNode(2)
        self.assertEqual(y, self.b.sibling)
        self.assertEqual(y.parent, self.T.root)
        
    def test_addNode_withoutSibling(self):
        """ Checking that we can add a Node to a childless parent. """
        z = self.T.createNode(3, self.a)
        self.assertEqual(z, self.a.child)
        self.assertEqual(z.parent, self.a)
        
    def test_getLeftSibling(self):
        """ Checking that we can find a Node's left-sibling. """
        c = self.T.createNode(3)
        self.assertEqual(c.getLeftSibling(), self.b)
        self.assertEqual(self.b.getLeftSibling(), self.a)
        self.assertIsNone(self.a.getLeftSibling())
            
    
if __name__ == "__main__":
    unittest.main()