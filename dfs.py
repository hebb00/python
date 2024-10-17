# Using a Python dictionary to act as an adjacency list
# graph = {
#   '5' : ['3','7'],
#   '3' : ['2', '4'],
#   '7' : ['8'],
#   '2' : [],
#   '4' : ['8'],
#   '8' : []
# }
from collections import defaultdict 

graph=defaultdict(list)
def AddNodes(graph ,parent, child):
    
    if parent not in graph:
      graph.update({parent:[child]})
    else:
      graph[parent].append(child)
        
visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
if __name__ == "__main__":
    AddNodes(graph,'5','6')
    AddNodes(graph,'6','7')
    AddNodes(graph, '7','2')
    AddNodes(graph, '7','8')
    print(graph)
    print("Following is the Depth-First Search")
    dfs(visited, graph, '5')