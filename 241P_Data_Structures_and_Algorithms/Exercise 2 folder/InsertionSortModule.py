"""To sort an array of size n in ascending order: 
1: Iterate from arr[1] to arr[n] over the array. 
2: Compare the current element (key) to its predecessor. 
3: If the key element is smaller than its predecessor, compare it to the 
elements before. Move the greater elements one position up to make space 
for the swapped element."""

class InsertionSort:
    def __init__(self):
        pass
    
    def sort(self, myList):
        i = 0
        while i < len(myList):
            #print("insertion ", i)
            j = i
            #compare with all values to the left
            while j > 0 and myList[j-1] > myList[j]:
                #swap values at j and j-1
                myList[j], myList[j-1] = myList[j-1], myList[j]
                j -= 1
            i += 1
        return myList