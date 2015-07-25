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
    
    def getLastSibling(self):
        x = self.sibling
        while x and x.sibling:
            x = x.sibling
        return x
        
    def getSiblings(self):
        ret = []
        x = self.sibling
        while x:
            ret.append(x)
            x = x.sibling
        return ret
        
    def findLeftSibling(self):
        if not self.getParent():
            return None
        left_candidate = self.getParent().child.sibling
        while(left_candidate and left_candidate.sibling is not self):
            left_candidate = left_candidate.sibling
        return left_candidate
        
    def getLastChild(self):
        return self.child.getLastSibling() if self.child else None
        
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
        
    def addNode(self, x, parent = None):
        """ Adds a node with key x to the given parent.
            If no parent specified, adds to root. """
        if not parent: parent = self.root
        y = parent.getLastChild()
        
        newNode = ArbitraryNode(x, None, None, parent)
        if y: y.sibling = newNode
        else: parent.child = newNode
        return
        
    def removeNode(self, node_in_tree):
        """ Removes a node and all child nodes. """
        if node_in_tree.isLeftmostSibling():
            if self.parent:
                self.parent.child = self.sibling
        else:
            leftSib = node_in_tree.findLeftSibling()
            leftSib.sibling = node_in_tree.sibling
        for kid in node_in_tree.getChildren():
            self.removeNode(kid)
        node_in_tree.killNode()
        