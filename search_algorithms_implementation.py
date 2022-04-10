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

def get_huristic_value(location_one,location_two):
    RADIUS=6373.0
    latitude_one = math.radians(location_one[0])
    longitude_one = math.radians(location_one[1])
    latitude_two = math.radians(location_two[0])
    longitude_two = math.radians(location_two[1])

    diffrence_in_longitude = longitude_two-longitude_one
    diffrence_in_latitude = latitude_two -latitude_one

    a = math.pow((math.sin(diffrence_in_latitude/2)),2) + math.cos(latitude_one)*math.cos(latitude_two)*math.pow((math.sin(diffrence_in_longitude/2)),2)
    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))

    distance_between = RADIUS * c
    return distance_between


def a_star_search(graph,start,end,city_cordinates):
    infinity=float('inf')
    nodes=dfs_generic(graph,start)
    search_data ={}
    
    if(end not in nodes):
        return []
    for node in nodes:
        search_data[node]={'F':infinity,'G':infinity,'from':None}

    search_data[start]['G']=0
    search_data[start]['F']=get_huristic_value(city_cordinates[start.node_identifier],city_cordinates[end.node_identifier])
    to_be_visited=[]
    visited=[]
    to_be_visited.append(start)
    while(len(to_be_visited)>0):
        smallest_f = infinity
        current_node = None
        for node in search_data:
            if(search_data[node]['F'] <= smallest_f and node  in to_be_visited):
                smallest_f=search_data[node]['F']
                current_node=node
        if(current_node==end):
            previous = search_data[current_node]['from']
            reconstructed_path=[]
            reconstructed_path.append(current_node)
            while (previous!=None):
                reconstructed_path.insert(0,previous)
                previous=search_data[previous]['from']
            return reconstructed_path
                
        for neighbour in graph.graph[current_node]['neighbours']:
            if (neighbour in visited):
                continue
            else:
                if( neighbour not in to_be_visited ):
                    to_be_visited.append(neighbour)
                if( (search_data[current_node]['G']+graph.graph[current_node]['neighbours'][neighbour]) < search_data[neighbour]['G'] ):
                    search_data[neighbour]['G']=search_data[current_node]['G']+graph.graph[current_node]['neighbours'][neighbour]
                    huristic_value = get_huristic_value(city_cordinates[neighbour.node_identifier],city_cordinates[end.node_identifier])
                    search_data[neighbour]['F']=search_data[neighbour]['G']+huristic_value
                    search_data[neighbour]['from']=current_node
        to_be_visited.remove(current_node)
        visited.append(current_node)
    return []

# add randome nodes to graph with specified size,
# geneate random edges between them,
# genearate random cordinates for the huristic value
def add_random_node_to_graph(graph,size,existing_city_coordinates):

    #generate random nodes
    new_nodes=[]
    for i in range(size):
        letters = string.ascii_lowercase
        random_word = ''.join(random.choice(letters) for i in range(7))
        node = Node(random_word)
        new_nodes.append(node)

    #create random edge
    for i in range(len(new_nodes)):
        node1 = new_nodes[random.randint(0,len(new_nodes)-1)]
        if(len(graph.graph.keys())>10):
            node2 = list(graph.graph.keys())[random.randint(0,(len(new_nodes) % len(graph.graph.keys())))]
        else:
            node2 = new_nodes[random.randint(0,len(new_nodes)-1)]
        edge = Edge(node1,node2)
        graph.add_edge(edge)

    #create random coordinates
    for i in new_nodes:
        latitude=(random.random() * 90)
        longitude=(random.random()*180)
        existing_city_coordinates[i.node_identifier]=[latitude,longitude]
    
    return graph,city_cordinates

