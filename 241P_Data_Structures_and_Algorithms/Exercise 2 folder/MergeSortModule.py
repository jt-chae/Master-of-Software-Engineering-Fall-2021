# -*- coding: utf-8 -*-
"""
 It divides the input array into two halves, calls itself for the two halves, 
 and then merges the two sorted halves. The merge() function is used for 
 merging two halves. The merge(arr, l, m, r) is a key process that assumes 
 that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted 
 sub-arrays into one.
"""

class MergeSort:
    def __init__(self):
        pass
            
    def sort(self, unsortedList):
        #do the sort here
        sortedList = [] #create a list to store the result of the sort
        if len(unsortedList) > 1:
            mid = len(unsortedList)//2 # Find the middle element of the list
            
            leftList = unsortedList[:mid] # Split the list into 2 halves
            rightList = unsortedList[mid:]
      
            self.sort(leftList) # Sorting the left half sublist
            self.sort(rightList) # Sorting the right half sublist
      
            i = j = k = 0 #initialize the indexs
      
            # Copy data to temporary sublists leftList[] and rightList[]
            while i < len(leftList) and j < len(rightList): 
                if leftList[i] < rightList[j]:
                    unsortedList[k] = leftList[i]
                    i += 1
                else:
                    unsortedList[k] = rightList[j]
                    j += 1
                k += 1
      
            # Checking if any element was left
            while i < len(leftList):
                unsortedList[k] = leftList[i]
                i += 1
                k += 1
      
            while j < len(rightList):
                unsortedList[k] = rightList[j]
                j += 1
                k += 1
        sortedList = unsortedList
        return sortedList
