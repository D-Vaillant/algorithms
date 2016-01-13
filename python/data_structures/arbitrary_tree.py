""" arbitrary_tree.py:
        Implementation of a tree with an arbitrary amount of children
        per node via the left-child, right-sibling system. """
        
import unittest

class Node:
    def __init__(self, k, c_ = None, s_ = None, p_ = None):
        if type(k) is Node:
            self.key = k.key
            self.child = k.child
            self.sibling = k.sibling
            self.parent = k.parent
        else:
            self.key = k
            self.child = c_
            self.sibling = s_
            self.parent = p_
    
    def __repr__(self):
        return "[NODE key={}]".format(self.key)
        
    def isInitialSibling(self):
        """ Returns True if there are no Nodes with this one as a sibling.
                Also returns True if the Node is an only sibling. """
        return not self.getParent() or (self.parent.child is self)
    
    def getInitialSibling(self):
        """ Returns a Node with the same parent that is the leftmost. """
        if self.getParent():
            return self.parent.child
        else:
            return None
            
    def getTerminalSibling(self):
        """ Returns a Node with the same parent that is the rightmost. """
        x = self
        while x.sibling:
            x = x.sibling
        return x
        
    def getSiblings(self):
        """ Returns an array of all the Node's siblings. Includes self. """
        ret = []
        x = self.getInitialSibling()
        while x:
            ret.append(x)
            x = x.sibling
        return ret
        
    def getPriorSibling(self):
        """ Returns a Node N such that N.sibling = self. """
        # Return nothing if the Node is the initial sibling.
        if self.isInitialSibling(): return None

        left_candidate = self.getInitialSibling()
        while(left_candidate.sibling is not self):
              left_candidate = left_candidate.sibling
        return left_candidate
        
    def getTerminalChild(self):
        """ Returns the rightmost child of the Node. """
        return self.child.getTerminalSibling() if self.child else None
        
    def getChildren(self):
        """ Returns an array of Nodes with self as their parent. """
        x = self.child
        return x.getSiblings() if x else []
        
    def getParent(self):
        """ Gets parent. """
        return self.parent
        
    def killNode(self):
        """ Wipes out all connections and key. """
        self.key = None
        self.parent = None
        self.child = None
        self.sibling = None
        
class ArbitraryTree:
    def __init__(self, root_val = None):
        self.root = Node(root_val)
        
    def defineRoot(self, x): 
        """ Defines the root as either x or a Node with key x.
            WARNING: Wipes out the tree below! """
        self.root = x if type(x) is Node else Node(x)
        
    def createNode(self, x, parent = None):
        """ Creates a node with key x with given parent.
            If no parent specified, adds to root. """  
        if parent is None: parent = self.root
        
        newNode = Node(x, None, None, parent)
        self.addNode(newNode, parent)
        return newNode
        
    def addNode(self, newNode, parent = None):
        """ Adds a node to the tree with given parent as right-most sibling.
            If no parent specified, adds to root. """
        if not parent: parent = self.root
        
        y = parent.getTerminalChild()
        
        if y: y.sibling = newNode
        else: parent.child = newNode
        newNode.parent = parent
        return newNode
        
    def removeNode(self, node_in_tree):
        """ Removes a node and all child nodes. """
        if node_in_tree.isInitialSibling():
            if node_in_tree.parent:
                node_in_tree.parent.child = node_in_tree.sibling
        else:
            leftSib = node_in_tree.getPriorSibling()
            leftSib.sibling = node_in_tree.sibling
        for kid in node_in_tree.getChildren():
            self.removeNode(kid)
        node_in_tree.killNode()

class TreeTester(unittest.TestCase):
    def setUp(self):
        """ Initialize! 
            T.root
             /
            a -- b """
        self.T = ArbitraryTree(99)
        self.a = Node(1)
        self.b = Node(2)
        
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
        self.assertIsNone(self.b.child)
        
    def test_isInitialSibling(self):
        """ Checking that we can find a Node's leftmost sibling. """
        self.assertTrue(self.a.isInitialSibling())
        self.assertFalse(self.b.isInitialSibling())
        
    def test_isInitialSibling_integrity(self):
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
        
    def test_getPriorSibling(self):
        """ Checking that we can find a Node's left-sibling. """
        c = self.T.createNode(3)
        self.assertEqual(c.getPriorSibling(), self.b)
        self.assertEqual(self.b.getPriorSibling(), self.a)
        self.assertIsNone(self.a.getPriorSibling())
            
if __name__ == "__main__":
    unittest.main()
