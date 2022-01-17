def main():
    fread = open('pride-and-prejudice.txt')
    fsearch = open('words-shuffled.txt')
    linesRead = fread.readlines() #Python file method readlines() reads until EOF using readline() and returns a list containing the lines
    linesSearch = fsearch.readlines() #Python file method readlines() reads until EOF using readline() and returns a list containing the lines
    # llset = LinkedListSet()
    # bset = BinaryTreeSet()
    # hset = HashTableSet()
    readWords = []
    testWords = []

    for line in linesRead:
        s = re.sub('[%s]' % re.escape(string.punctuation), ' ', line)
        listRead = s.split()
        for word in listRead:
            readWords.append(word)

    for line in linesSearch:
        listSearch = line.split()
        testWords.append(listSearch[0])

    file = Workbook(encoding = 'utf-8')
    table1 = file.add_sheet('LinkedListSet')
    table2 = file.add_sheet('BinarySearchTreeSet')
    table3 = file.add_sheet('HashTableSet')
    data1 = [None]*21
    data2 = [None]*21
    data3 = [None]*21

    lenData = []

    for i in range(0,10):
        data1[i],data1[11+i],_ = experiment(readWords,testWords,LinkedListSet())
        data2[i],data2[11+i],_ = experiment(readWords,testWords,BinaryTreeSet())
        data3[i],data3[11+i],_ = experiment(readWords,testWords,HashTableSet())
    _,_,lenData = experiment(readWords,testWords,HashTableSet())
    for i,p in enumerate(data1):
        if p:
            for j,q in enumerate(p):
                if q:
                    print("q row: ",j+2, "q colum: ",i+1, "q data:", q)
                    table1.write(j+2,i+1,q)
    for i,p in enumerate(data2):
        if p:
            for j,q in enumerate(p):
                if q:
                    table2.write(j+2,i+1,q)
    for i,p in enumerate(data3):
        if p:
            for j,q in enumerate(p):
                if q:
                    table3.write(j+2,i+1,q)
    for i,d in enumerate(lenData):
        table1.write(i+2,0,d)
        table2.write(i+2,0,d)
        table3.write(i+2,0,d)
    file.save('output.xls')

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

#Node class
class ListNode:
    # Function to initialize the node object
    def __init__(self, data=None, next=None):
        self.data = data # Assign data
        self.next = next #Initialize pointer "next" as "None"


#Linked List class
class LinkedListSet:
    # Function to create and initialize the Linked List object
    def __init__(self):
        self.size = 0
        self.head = ListNode(0) #The only information I need to store for a linked list is where the list starts (the head of the list)
        self.tail = ListNode(0) #start with an empty list
        self.head.next = self.tail #initialize pointer

    def __len__(self): #function to measure the length of the Linked List object, this will run when the object is created
        return self.size #return

    def size(self): #function to measure the size of the Linked List object "self"
        return self.size

    def __contains__(self, data): #check if the Linked List object "self" contains the data or not
        return self.contains(data) #return a boolean value True or False

    def contains(self, data): #search function
        data = str(data) #convert value to string data type
        node = self.head #initialize the first node of the Linked List
        while node.next != self.tail: #when the list is not at the end yet
            node = node.next #go to the next node
            if node.data == data: #if the word is in the node, then return True
                return True
        return False

    def boolean_add(self, data):#Takes a word as input and adds the word to the set if the word is not already there.
        data = str(data) #convert to "str" data type
        if self.contains(data): #check if the word is already in the list or not
            return False #if the word is already in the list, then return F
        node = self.head #initialize the first node with the head of the list
        while node.next != self.tail: #when the node is not at the end of the list yet
            node = node.next #pointer to go to the next node
        node.next = ListNode(data, self.tail)
        self.size += 1 #increase the size of the linked list by 1
        return True #Returns true if the word was added

    def __str__(self): #The __str__ method is called when the print() or str() are invoked on the object and return a string
        res = '['
        node = self.head
        while node.next != self.tail:
            node = node.next
            res += node.data + ','
        return res[:-1] + ']'

class BinaryTreeSet:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def size(self):
        return self.size

    def __contains__(self, data):
        return self.contains(data)

    def contains(self, data):
        data = str(data)
        node = self.root
        while node: #sorting data left node and right node
            if node.data > data: #node’s left child must have a key less than its parent
                node = node.left #pointer to go left
            elif node.data < data: #and node’s right child must have a key greater than or equal to its parent
                node = node.right #pointer to go right
            else:
                return True
        return False

    def boolean_add(self, data): #adding data to the binary tree
        data = str(data) #convert data to string type
        if not self.root: #create the first node of the Binary Tree if there is no root yet
            self.root = TreeNode(data)
            self.size += 1
            return True
        node = self.root #create the first node of the Binary Tree from the root
        while node:
            if node.data > data: #node’s left child must have a key less than its parent
                if not node.left: #create the first left child of the root if there is no left child yet
                    node.left = TreeNode(data) #pointer to left child, create tree node object with data
                    self.size += 1
                    return True
                node = node.left
            elif node.data < data: #node’s right child must have a key greater than or equal to its parent
                if not node.right:
                    node.right = TreeNode(data)  #create the first right child of the root if there is no right child yet
                    self.size += 1
                    return True
                node = node.right
            else:
                return False

    def __str__(self):
        node = self.root
        res = '['
        while node:
            if node.left:
                pre = node.left
                while pre.right and pre.right != node:
                    pre = pre.right
                if pre.right:
                    pre.right = None
                    res += node.data + ','
                    node = node.right
                else:
                    pre.right = node
                    node = node.left
            else:
                res += node.data + ','
                node = node.right
        return res[:-1] + ']'


class HashTableSet:
    def __init__(self):
        self.numOfSlots = 10000
        self.cell = [None]*self.numOfSlots
        self.size = 0

    def __len__(self):
        return self.size

    def size(self):
        return self.size

    def __contains__(self, data):
        return self.contains(data)

    def contains(self, data):
        data = str(data)
        index = hash(data) % self.numOfSlots
        if not self.cell[index]:
            return False
        else:
            node = self.cell[index]
            while node:
                if node.data == data:
                    return True
                node = node.next
            return False

    def boolean_add(self, data):
        data = str(data)
        index = hash(data) % self.numOfSlots
        if not self.cell[index]:
            self.cell[index] = ListNode(data)
            self.size += 1
            return True
        else:
            node = self.cell[index]
            while node:
                if node.data == data:
                    return False
                if not node.next:
                    node.next = ListNode(data)
                    self.size += 1
                    return True
                node = node.next

    def __str__(self):
        res = '['
        for i in range(self.numOfSlots):
            node = self.cell[i]
            while node:
                res += node.data + ','
                node = node.next
        return res[:-1] + ']'

from xlwt import *
import string,re,time,xlwt


def experiment(dictionary,test,mySet):
    obj = time.gmtime(0)  #Convert the current time in seconds since the epoch to a time.struct_time object in UTC
    epoch = time.asctime(obj) #The epoch is the point where the time starts. Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string of the following form: 'Sun Jun 20 23:21:05 1993'
    addData = [] #create a list
    checkData = [] #create list
    lenData = [] #create list
    count = 0
    for word in dictionary:
        if count % 10 == 0:
            lenData.append(len(mySet)) #extend the size of the lenData list
            start_time = time.monotonic_ns() #method of time module in Python is used to get the value of a monotonic clock in nanoseconds
#             print("lenData is: ", lenData)
        mySet.boolean_add(word) #add the word to the linked list
#         print(mySet)
        if count % 10 == 0:
            end_time = time.monotonic_ns()
            addData.append(end_time - start_time)
        count += 1

    myCount = 0
    count = 0
    for t in test:
        count += 1
        start_time = time.monotonic_ns()
        check = mySet.contains(t)
        end_time = time.monotonic_ns()
        checkData.append(end_time-start_time)
        if not check:
            myCount += 1
    time4 = time.monotonic_ns()
    #print(len(mySet),myCount)
    print("The number of non-repeated words that are present in the set: ", len(mySet))
    print("How many words do not exist in the set: ", myCount)
    return(addData,checkData,lenData)

# def test():
#     nums = [1,2,3,4,1,2,31,23,2,1,24,12,3,'aaa','asdasda','asdasd','aaa']
#     print('LinkedListSet Test')
#     print('')
#     set1 = LinkedListSet()
#     for num in nums:
#         print(num,set1.boolean_add((num)))
#     print("The size of the Linked List Set: ", len(set1))
#     print("Linked List Set 1: ",set1)
#     print("Does this linked list set 1 contain (1) ?", set1.contains((1)))
#     print("Does this linked list set 1 contain '99'?", set1.contains((99)))
#     print((31) in set1)
#     print('')
#     print('BinaryTreeSet Test')
#     print('')
#     set2 = BinaryTreeSet()
#     for num in nums:
#         print(num, set2.boolean_add(num))
#     print(len(set2))
#     print(set2)
#     print(set2.contains(1))
#     print(set2.contains(9))
#     print(31 in set2)
#     print('')
#     print('HashTableSet Test')
#     print('')
#     set3 = HashTableSet()
#     for num in nums:
#         print(num, set3.boolean_add((num)))
#     print(len(set3))
#     print(set3)
#     print(set3.contains(1))
#     print(set3.contains(9))
#     print(31 in set3)

if __name__ == "__main__":
    main()
#     test()
