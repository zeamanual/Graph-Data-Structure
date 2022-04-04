import math
from graph_implemenation import Edge, Node,graph,city_cordinates
import random
import string


Infinity=float('inf')
def bfs(graph,start_node,end_node):

    visited=[]
    parent={}
    parent[start_node]=None
    tobe_visited=[start_node]
    while len(tobe_visited) > 0:
        if(start_node==end_node):
            return [start_node,end_node]
        if(tobe_visited[0] not in visited):
            visited.append(tobe_visited[0])
            for neighbour in graph.graph[tobe_visited[0]]['neighbours'].keys():
                if(neighbour==end_node):
                    parent[neighbour]=tobe_visited[0]
                    current_parrent = parent[neighbour]
                    path=[neighbour]
                    while (current_parrent != None):
                        path.append(current_parrent)
                        current_parrent=parent[current_parrent]
                    path.reverse()
                    return path
                if(neighbour not in visited and (neighbour not in tobe_visited)):
                    tobe_visited.append(neighbour)
                    parent[neighbour]=tobe_visited[0]
        tobe_visited.pop(0)
    return []

def dfs(graph,start_node,end_node,visited = []):
    visited.append(start_node)
    if(start_node==end_node):
        return visited
    for i in graph.graph[start_node]['neighbours'].keys():
            if i not in visited:
               return dfs(graph,i,end_node,visited=visited)
    print(start_node)
    return []

def dfs(graph,start_node,end_node):
    visited=[]
    to_be_visited=[]
    to_be_visited.append(start_node)
    while(len(to_be_visited)>0 ):
        current_node = to_be_visited.pop()
        if(current_node==end_node):
                return visited
        if(current_node not in visited):
            for neighbour in graph.graph[current_node]['neighbours'].keys():
                if(neighbour not in to_be_visited):
                    to_be_visited.append(neighbour)
            visited.append(current_node)
    return visited

def dfs_generic(graph,node):
    visited=[]
    to_be_visited=[]
    to_be_visited.append(node)
    while(len(to_be_visited)>0):
        current_node = to_be_visited.pop()
        if(current_node not in visited):
            for neighbour in graph.graph[current_node]['neighbours'].keys():
                if(neighbour not in to_be_visited):
                    to_be_visited.append(neighbour)
            visited.append(current_node)
    return visited

def dijkstra(graph,start_node,end_node):
    Infinity = float('inf')
    result = {}
    visited = []
    nodes = dfs_generic(graph,start_node)
    for nd in nodes:
        result[nd]={'shortest_distance':Infinity, 'via':None}
    result[start_node]['shortest_distance']=0
    shortest_distance=Infinity
    shortest=start_node
    while(len(visited)<len(nodes)):
        for nd in result.keys():
            if((result[nd]['shortest_distance']<=shortest_distance) and (nd not in visited)):
                shortest_distance=result[nd]['shortest_distance']
                shortest=nd
        for neighbour in graph.graph[shortest]['neighbours'].keys():
            if(result[neighbour]['shortest_distance'] > graph.graph[shortest]['neighbours'][neighbour]+result[shortest]['shortest_distance']):
                result[neighbour]['shortest_distance']=graph.graph[shortest]['neighbours'][neighbour]+result[shortest]['shortest_distance']
                result[neighbour]['via']=shortest;
        visited.append(shortest)
        shortest_distance=Infinity
    path=[]
    path.append(end_node)
    previous=result[end_node]['via']
    while (previous != None):
        path.append(previous)
        previous=result[previous]['via']
    path.reverse()
    return path
