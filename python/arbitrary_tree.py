""" arbitrary_tree.py:
        Implementation of a tree with an arbitrary amount of children
        per node via the left-child, right-sibling system. """
            
class ArbitraryNode:
    def __init__(self, k, c_ = None, s_ = None, p_ = None):
        self.key = k
        self.child = c_
        self.sibling = s_
        self.parent = p_
    
    def isLeftmostSibling(self):
        return self.parent and self.parent.child is self
    
    def getInitialSibling(self):
        if self.getParent():
            return self.parent.child
        else:
            return self
            
    def getTerminalSibling(self):
        x = self
        while x.sibling:
            x = x.sibling
        return x
        
    def getSiblings(self):
        ret = []
        x = self.sibling
        while x:
            ret.append(x)
            x = x.sibling
        return ret
        
    def getLeftSibling(self):
        if not self.getParent():
            return None
        left_candidate = self.getInitialSibling()
        if left_candidate is self: return self
        else:
            while(left_candidate.sibling is not self and left_candidate):
                left_candidate = left_candidate.sibling
        return left_candidate if left_candidate.sibling is self \
                              else None
        
    def getTerminalChild(self):
        return self.child.getTerminalSibling() if self.child else None
        
    def getChildren(self):
        ret = []
        x = self.child
        if x:
            ret.append(x)
            ret.extend(x.getSiblings())
        return ret
        
    def getParent(self):
        return self.parent
        
    def killNode(self):
        self.parent = None
        self.child = None
        self.sibling = None
        
class ArbitraryTree:
    def __init__(self, root_val = None):
        self.root = ArbitraryNode(root_val)
        
    def defineRoot(self, x): 
        """ Defines the root as a node with key x.
            WARNING: Wipes out the tree below!" """
        self.root = ArbitraryNode(x)
        
    def createNode(self, x, parent = None):
        """ Creates a node with key x with given parent.
            If no parent specified, adds to root. """        
        newNode = ArbitraryNode(x, None, None, parent)
        self.addNode(newNode, parent)
        return
        
    def addNode(self, newNode, parent = None):
        """ Adds a node to the tree with given parent as right-most sibling.
            If no parent specified, adds to root. """
        if not parent: parent = self.root
        
        y = parent.getTerminalChild()
        
        if y: y.sibling = newNode
        else: parent.child = newNode
        newNode.parent = parent
        return
        
    def removeNode(self, node_in_tree):
        """ Removes a node and all child nodes. """
        if node_in_tree.isLeftmostSibling():
            if node_in_tree.parent:
                node_in_tree.parent.child = node_in_tree.sibling
        else:
            leftSib = node_in_tree.getLeftSibling()
            leftSib.sibling = node_in_tree.sibling
        for kid in node_in_tree.getChildren():
            self.removeNode(kid)
        node_in_tree.killNode()
    
def testTree(x):
    return ArbitraryTree(x)
   
def testNode(x):
    return ArbitraryNode(x)
    
n = testTree(5)
a = testNode(1)
b = testNode(2)
c = testNode(3)
n.addNode(a)
n.addNode(b)
n.addNode(c)
#assert n.root.getChildren() == [a, b, c]