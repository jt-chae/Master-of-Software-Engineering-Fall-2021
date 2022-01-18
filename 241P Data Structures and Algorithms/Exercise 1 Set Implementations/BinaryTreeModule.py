
    
class BinaryTreeNode:
    def __init__(self, value=None): #initiate the binary tree object
        self.value = value #initialize the parent
        self.left = None #initialize the left pointer to None
        self.right = None #initialize the right pointer to None
        
    def add(self, value): #function to add a word to the Binary Tree object
        # If there is no value yet, initialize with this one
        if self.value == None:
            self.value = value
            return True
        # If this value already exists do not add
        if value == self.value:
            return False
        isRight = (value > self.value) #return True/False 
        if isRight: 
            if not self.right: #if no right child, create one
                self.right = BinaryTreeNode(value)
            else:
                self.right.add(value) #go back to def add (recursive)
        else:
            if not self.left:
                self.left = BinaryTreeNode(value)
            else:
                self.left.add(value)
        return True
    
    def contains(self, value):
        if value == self.value: #check if the word exists in the tree
            return True
        if value > self.value:  #if the word is bigger than the node value
            if self.right is None: #if there is no right node
                return False
            else:
                return self.right.contains(value) #if there is a right node, return its value
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value) 
            
    def size(self):
        s = 1
        if self.left:#if there is a node on the left
            s += self.left.size() #add 1 to s, then pause and go to the next node
        if self.right:
            s += self.right.size()
        return s