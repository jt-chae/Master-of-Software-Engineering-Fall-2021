# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 22:08:28 2021

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

def AdjListsToIncidenceMat(adjLists):
    listOfEdges = [] #this list will store pairs of vertices
    #first create list of all unique edges
    for adjList in adjLists:
        v1 = adjList[0] #assig v1 to the first element in the Adjlist list by indexing 
        for i in range(1,len(adjList)): #i starts at 1 b/c v1 is already i = 0
            v2 = adjList[i] #go thru the list (horizontally)
            edge = [v1,v2] #create the edge by creating a list of vertices v1 and v2
            #lower vertex is the first element in the list, to make sure edges are unique
            edge = [min(edge),max(edge)]
            if edge not in listOfEdges: #check for uniqueness of the edge in the list
                listOfEdges.append(edge)
    #number of verts is the max value in the edges + 1 b/c we start at 0
    numVerts = max([max(edge) for edge in listOfEdges])+1
    numRows = numVerts #n rows
    numCols = len(listOfEdges) #m columns
    #incidence mat is n rows by m columns
    incidenceMat = [[0]*numCols for i in range(numRows)]
    #create the incidence matrix
    for i in range(len(listOfEdges)): #i is the columns (edges) of the matrix
        v1,v2 = listOfEdges[i][0], listOfEdges[i][1] #get values v1 (at row i, column 0); and v2 (at row i, column 1) from the listOfEdges
        #print("v1, v2: ", v1, v2)
        incidenceMat[v1][i] = 1 #row v1 (vertice), column i (edge), eg: v1 = 0, i = 0 for first run
        incidenceMat[v2][i] = 1 #row v2 (vertice), column i (edge), eg: v2 = 1, i = 0 for first run
    return incidenceMat

print("Adjacency List")
print(exampleAdjLists)
print("Result - Incidence Mat")
print(AdjListsToIncidenceMat(exampleAdjLists))
print("""Time complexity
There are for loops so most likely this is the upper bound 
        for adjList in adjLists: 1 for every vertex: n time
           for i in range(1,len(adjList)): for every entry in the adjList: 1 every edge: m time
    final time complexity is 0(n*m)""")