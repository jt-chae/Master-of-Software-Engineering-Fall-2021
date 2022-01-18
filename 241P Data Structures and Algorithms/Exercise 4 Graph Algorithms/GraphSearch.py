
import random
import queue

adjLists = {'A': ['B', 'E'],
            'B': ['A', 'C', 'F'],
            'C': ['B', 'D', 'G'],
            'D': ['C', 'H'],
            'E': ['A', 'F', 'I'],
            'F': ['B', 'E', 'G', 'J'],
            'G': ['C', 'F', 'H', 'K'],
            'H': ['D', 'G', 'L'],
            'I': ['E', 'J', 'M'],
            'J': ['F', 'I', 'K', 'N'],
            'K': ['G', 'J', 'L', 'O'],
            'L': ['H', 'K', 'P'],
            'M': ['I', 'N'],
            'N': ['J', 'M', 'O'],
            'O': ['K', 'N', 'P'],
            'P': ['L', 'O']
            }

print(adjLists)

def breadthSearch(startVertex):
    print('Start vertex {}'.format(startVertex)) 
    visitedVertices = []
    vertexQueue = queue.Queue() #create a queue class object
    
    vertexQueue.put(startVertex) #create the queue with the first node (letter A)
    visitedVertices.append(startVertex) #cross out the vertice that we just visited
    
    while not vertexQueue.empty(): #if the queue is not empty yet
        vertex = vertexQueue.get() #get the next value in the queue
        connectedVertices = adjLists[vertex] #get all the vertices that this current vertex is connected to by indexing into the adjList row
        for nextVertex in connectedVertices:
            if nextVertex not in visitedVertices:
                print('Visit vertex {} from {}'.format(nextVertex, vertex))
                visitedVertices.append(nextVertex) #add the visited nodes to the list of visited nodes
                vertexQueue.put(nextVertex)  #add the visited nodes to the queue object
    #go until there is nothing left in the queue
    
print('Breadth first search:')
breadthSearch('A')

def depthSearch(startVertex):
    print('Start vertex {}'.format(startVertex))
    visitedVertices = [] #to avoid going back to the vertex we have already visited
    
    def visitVertex(vertex): #function to traverse thru the graph by visiting each unvisited vertex
        visitedVertices.append(vertex) 
        connectedVertices = adjLists[vertex] #get all the vertexes that this vertex is connected to by indexing into the row of the dictionary adjLists
        for nextVertex in connectedVertices: #go into the list of vertices connected to the selected vertex
            if nextVertex not in visitedVertices:#if this vertex has not been visited yet
                print('Visit vertex {} from {}'.format(nextVertex, vertex))
                visitVertex(nextVertex) #call recursively, after A, now call B, go back to line 49
                
    visitVertex(startVertex) #start the search by visiting first vertex 
    
print('Depth first search:')
depthSearch('A')