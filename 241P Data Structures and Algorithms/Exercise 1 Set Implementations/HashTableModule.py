

# simple has function that adds together all characters in a string
def hashFunction(s):
    key = 0
    for char in s:
        key += ord(char)
    return key

class HashTable:
    def __init__(self):
        self.buckets = {} #create a dictionary to store the buckets
        self.count = 0
    def add(self, value):
        key = hashFunction(value)
        # Check for collision
        if key in self.buckets: #check if the key is in the bucket dictionary
            bucket_value = self.buckets[key] #index into the bucket dictionary using the key to get its corresponding value
            if value in bucket_value: #if the word we want to add is already in the bucket
                return False #get out of the function
            self.buckets[key].append(value) #add our word to the bucket
        else:
            self.buckets[key] = [value] #create a bucket with the key and our value (word to add)
        self.count += 1 #keep track of the number of words we have
        return True
    def contains(self, value): 
        key = hashFunction(value) #generate a key using the hashFunction
        if key in self.buckets: #if the key is in the bucket dictionary
            bucket_value = self.buckets[key] #index into the bucket dictionary using the key to get its corresponding value
            if value in bucket_value: #check to see our word is the same as the word already in the bucket value
                return True
        return False
    
    def size(self):
        return self.count
