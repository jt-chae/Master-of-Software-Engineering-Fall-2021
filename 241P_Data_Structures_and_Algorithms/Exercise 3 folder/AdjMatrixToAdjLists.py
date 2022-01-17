# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 21:35:19 2021

@author: Jennifer
"""

exampleMat = [[0,1,0,0,1],
              [1,0,1,1,1],
              [0,1,0,1,0],
              [0,1,1,0,1],
              [1,1,0,1,0]] #vertices row vs vertices column

exampleAdjLists = [[0, 1, 4], 
                   [1, 0, 2, 3, 4], 
                   [2, 1, 3], 
                   [3, 1, 2, 4], 
                   [4, 0, 1, 3]]

def AdjMatToAdjLists(mat):
    adjLists = []
    for i in range(len(mat)): #go thru every row
        row = mat[i] #store the row we got from matrix mat
        adjList = [i] #create a list, put the first number in, start with the matrix row number, says row 0 for the first run and so on
        for j in range(len(row)):
            value = row[j] #create a list, start with the first column number
            if value == 1: #if the vertices intersect, then add tp adjList list
                adjList.append(j) 
        adjLists.append(adjList)
    return adjLists

print("Adjacency Matrix")
print(exampleMat)
print("Result - Adjacency List")
print(AdjMatToAdjLists(exampleMat))
print("Time complexity is O(n^2) where n is the number of vertices")