# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 22:09:43 2021

@author: Jennifer
"""

exampleIncidenceMat = [[1,1,0,0,0,0,0],
                       [1,0,1,1,1,0,0],
                       [0,0,0,1,0,1,0],
                       [0,0,0,0,1,1,1],
                       [0,1,1,0,0,0,1]]

exampleAdjLists = [[0, 1, 4], 
                   [1, 0, 2, 3, 4], 
                   [2, 1, 3], 
                   [3, 1, 2, 4], 
                   [4, 0, 1, 3]]

def IncidenceMatToAdjLists(mat):
   
    numRows = len(mat) #number of vertices is number of row of matrix
    adjLists = [[i] for i in range(numRows)] #number of rows in mat is number of row in adj list 
    numCols = len(mat[0]) #the length of one row is the number of how many columns in the matrix 
   
    for i in range(numCols): #iterate thru the columns of incidence matrix
        tempList = []
        for j in range(numRows): #iterate thru every row in the i colum and see if the row has a 1
            val = mat[j][i] #get the value 1 or 0 from the matrix
            if val == 1: #check if the value is 1
                tempList.append(j) #append row number to the list of pairs v1,v2 that will become adjList
        #create the Adj list
        v1 = tempList[0] 
        v2 = tempList[1]
        adjLists[v1].append(v2)  #make a pair
        adjLists[v2].append(v1) 
        
    
    return adjLists

    

print("Incidence Matrix")
print(exampleIncidenceMat)
print("Result - Adjacency List")
print(IncidenceMatToAdjLists(exampleIncidenceMat))
print("""Time complexity 
for i in range(numCols): go thru every edge, m times
    for j in range(numRows): go thru every vertex, n times
        O(n*m)""")