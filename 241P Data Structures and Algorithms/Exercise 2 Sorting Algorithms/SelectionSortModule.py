
"""
The selection sort algorithm sorts an array by repeatedly finding the 
minimum element (considering ascending order) from unsorted part and putting 
it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering 
ascending order) from the unsorted subarray is picked and moved to the sorted 
subarray.
"""

class SelectionSort:
    def __init__(self):
        pass
            
    def sort(self, unsortedList):
        #do the sort here
        sortedList = [] #create a list to store the result of the sort
        # Traverse through all array elements
        for i in range(len(unsortedList)):
            #print("selection ", i)
            # Find the minimum element in remaining 
            # unsorted array
            min_idx = i
            for j in range(i+1, len(unsortedList)):
                if unsortedList[min_idx] > unsortedList[j]:
                    min_idx = j
                      
            # Swap the found minimum element with 
            # the first element        
            unsortedList[i], unsortedList[min_idx] = unsortedList[min_idx], unsortedList[i]
        sortedList = unsortedList
        return sortedList
