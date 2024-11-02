# Python program for 
# validation of a graph 

# import dictionary for graph 
from collections import defaultdict 

# function for adding edge to graph 
graph = {}
def addEdge(graph,u,v): 
	graph[u].append(v) 

# definition of function 
def generate_edges(graph): 
	edges = [] 

	# for each node in graph 
	for node in graph: 
		
		# for each neighbour node of a single node 
		for neighbour in graph[node]: 
			
			# if edge exists then append 
			edges.append((node, neighbour)) 
	return edges 

def dfs(graph, visited = None):
    if visited is None:
        visited = set()
  
    visited.add(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            found = dfs(graph, neighbour, search_value, visited)

    return False
   
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

	
    
start = "F"
search_value = "Z"
res = dfs(graph, start, search_value)
print(f"element {search_value} : {res}")
if __name__ == "__main__":


	addEdge(graph,'b','e') 
	addEdge(graph,'c','d') 
	addEdge(graph,'c','e') 
	addEdge(graph,'c','a') 
	addEdge(graph,'c','b') 
	addEdge(graph,'e','b') 
	addEdge(graph,'d','c') 
	addEdge(graph,'e','c') 

	# Driver Function call 
	# to print generated graph 
	print(generate_edges(graph)) 
