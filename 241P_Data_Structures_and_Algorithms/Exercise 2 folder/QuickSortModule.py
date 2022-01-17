"""
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an 
element as pivot and partitions the given array around the picked pivot. 
There are many different versions of quickSort that pick pivot in different 
ways. 
"""
class QuickSort:
    def __init__(self):
        pass
    
    def sort(self, myList):
        if len(myList) <= 1: #when to stop the recursion is when the list only contains 1 element
            return myList 
        pivotIdx = int(len(myList)/2) #split the list into 2 
        pivot = myList[pivotIdx] #index into the list to get the value of pivot
        #print('{} - "{}"'.format(pivotIdx, pivot)) 
        first_half = self.sort([x for x in myList if x < pivot]) #recursively put words less than the pivot to the left list
        middle = [x for x in myList if x == pivot] #store all the words that are equal to the pivot into a list to save memory
        second_half = self.sort([x for x in myList if x > pivot]) #recursively put words more than the pivot to the right list
        return first_half + middle + second_half
     