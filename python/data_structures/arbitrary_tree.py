""" arbitrary_tree.py:
        Implementation of a tree with an arbitrary amount of children
        per node via the left-child, right-sibling system. """
        
class ArbitraryNode:
    def __init__(self, k, c_ = None, s_ = None, p_ = None):
        self.key = k
        self.child = c_
        self.sibling = s_
        self.parent = p_
    
    def __repr__(self):
        return "[NODE key={}]".format(self.key)
        
    def isLeftmostSibling(self):
        """ Returns True if there are no Nodes with this one as a sibling. """
        if self.getParent(): return (self.parent.child == self)
        else: return False
    
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
        
    def getLeftSibling(self):
        """ Returns a Node N such that N.sibling = self. """
        if not self.getParent():
            return None
        left_candidate = self.getInitialSibling()
        if left_candidate is self: return None
        else:
            while(left_candidate.sibling is not self and left_candidate):
                left_candidate = left_candidate.sibling
        return left_candidate if left_candidate.sibling is self \
                              else None
        
    def getTerminalChild(self):
        """ Returns the rightmost child of the Node. """
        return self.child.getTerminalSibling() if self.child else None
        
    def getChildren(self):
        """ Returns an array of Nodes N[] s.t. n in N iff n.parent = self """
        ret = []
        x = self.child
        if x:
            ret.extend(x.getSiblings())
        return ret
        
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
        self.root = ArbitraryNode(root_val)
        
    def defineRoot(self, x): 
        """ Defines the root as a node with key x.
            WARNING: Wipes out the tree below!" """
        self.root = ArbitraryNode(x)
        
    def createNode(self, x, parent = None):
        """ Creates a node with key x with given parent.
            If no parent specified, adds to root. """  
        if parent is None: parent = self.root
        
        newNode = ArbitraryNode(x, None, None, parent)
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
        if node_in_tree.isLeftmostSibling():
            if node_in_tree.parent:
                node_in_tree.parent.child = node_in_tree.sibling
        else:
            leftSib = node_in_tree.getLeftSibling()
            leftSib.sibling = node_in_tree.sibling
        for kid in node_in_tree.getChildren():
            self.removeNode(kid)
        node_in_tree.killNode()