#Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data=None, next=None):
        self.data = data # Assign data
        self.next = next #Initialize pointer "next" as "None"
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 #number of nodes in the list
   
    def add_item(self, data):
        if self.contains(data):
            return False
        if self.size == 0:
            new_node = Node(data)
            new_node.next = None
            self.head = new_node
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.next = None
            self.tail.next = new_node #the last node from before now will point to this new node
            self.tail = new_node
        self.size += 1
        return True
    
    def contains (self, check_data):
        temp = self.head #first node of the list
        while temp is not None: #instead of comparing to self.tail, we compare to None so that it checks the data of self.tail too
            if temp.data == check_data:
                return True #the method would end here, contains will return True right away
            temp = temp.next
        return False #if we have gone thru the whole list and did not find any match
    
    def size(self):
        return(self.size)
    


