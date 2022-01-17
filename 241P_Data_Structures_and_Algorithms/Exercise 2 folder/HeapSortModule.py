"""
1. Build a max heap from the input data. 
2. At this point, the largest item is stored at the root of the heap. Replace 
it with the last item of the heap followed by reducing the size of heap by 1. 
Finally, heapify the root of the tree. 
3. Repeat step 2 while the size of the heap is greater than 1.
"""
class HeapSort:
    def __init__(self):
        pass
    
    def sort(self, myList):
        # To heapify subtree rooted at index i.
        # n is size of heap
        def heapify(arr, n, i):
            largest = i  # Initialize largest as root
            l = 2 * i + 1     # left = 2*i + 1
            r = 2 * i + 2     # right = 2*i + 2
          
            # Test if left child of root exists and is
            # greater than root
            if l < n and arr[i] < arr[l]:
                largest = l
          
            # Test if right child of root exists and is
            # greater than root
            if r < n and arr[largest] < arr[r]:
                largest = r
          
            # Change root, if needed
            if largest != i:
                arr[i],arr[largest] = arr[largest],arr[i]  # swap
          
                # Heapify the root.
                heapify(arr, n, largest)
                
        n = len(myList)      
        # Build a maxheap.
        # Since last parent will be at ((n//2)-1) we can start at that location.
        for i in range(n // 2 - 1, -1, -1):
            heapify(myList, n, i)
      
        # One by one extract elements
        for i in range(n-1, 0, -1):
            myList[i], myList[0] = myList[0], myList[i]   # swap
            heapify(myList, i, 0)
            
        return myList