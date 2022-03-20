
import math
Infinity=float('inf')

class Graph:
    def __init__(self):
         self.graph={}
         
    def add_node(self,node):
        if node not in self.graph.keys():
            self.graph[node] = {'neighbours':{}}
        else:
            print(f'{node.node_identifier} node already exists')
    
    def remove_node(self,node):
        if(node in self.graph.keys()):
            self.graph.pop(node)
            for existing_node, neighbour in self.graph.items():
                if(node.node_identifier in self.graph[existing_node]['neighbours'].keys()):
                    self.graph[existing_node]['neighbours'].pop(node)
        else:
            print("Node doesn't exist")
        

    def add_edge(self,edge ):
        
        first_node , second_node = edge.edge
        if(first_node not in self.graph.keys()):
            self.add_node(first_node)

        if(second_node not in self.graph.keys()):
            self.add_node(second_node)
        if(edge.directed):
            if(second_node not in self.graph[first_node]['neighbours'].keys() ):
                self.graph[first_node]['neighbours'][second_node]=edge.weight
            else:
                print("edge already exists")
        else:
            if((first_node not in self.graph[second_node]['neighbours'].keys() ) and (second_node not in self.graph[first_node]['neighbours'].keys() )):
                self.graph[first_node]['neighbours'][second_node]=edge.weight
                self.graph[second_node]['neighbours'][first_node]= edge.weight
            else: 
                print('edge alrady exists')
    def remove_edge(self,edge):
        first_node , second_node = edge.edge
        if(first_node in self.graph.keys() and second_node in self.graph.keys() ):
            if(first_node in self.graph[second_node]['neighbours'] or second_node in self.graph[first_node]['neighbours'] ):
                if( first_node in self.graph[second_node]['neighbours']):
                    self.graph[second_node]['neighbours'].pop(first_node)
                if(second_node in self.graph[first_node]['neighbours']):
                    self.graph[first_node]['neighbours'].pop(second_node)
            else:
                print("edge doeen't exist")
        else:
            print("Node does not exist in the graph")

    def __str__(self):
        detail=''
        for node,neighbour in self.graph.items():
            detail+=f"{node.node_identifier}: [ "
            # {neighbour['neighbours']} \n"
            for neigh in neighbour['neighbours'].keys():
                detail+= f"{neigh.node_identifier}, "
            detail += " ] \n"
        return  detail   


class Edge:
     def __init__(self,node_one,node_two,directed=False,weight=1):
         self.edge= (node_one,node_two)
         self.directed = directed
         self.weight=weight

     def __str__(self):
        first, second = self.edge
        return f'{first.node_identifier} - {second.node_identifier} -> weight: {self.weight} directed: {self.directed}'

class Node:
    def __init__(self,node_identifier):
        self.node_identifier = node_identifier;

    def __str__(self):
        return f'{self.node_identifier}'

 #load all data from file
def load_data(graph):
    
    #reading contents from city connection file and load to graph
    connection_file = open('city connection.txt','r')
    global loaded_nodes
    loaded_nodes=[]
    read_line= connection_file.readline()
    while(read_line):
        data =read_line.split(',')
        node1 = None
        node2 = None
        first_node_already_exists = False
        second_node_already_exists = False
        for node in loaded_nodes:
            if(node.node_identifier == data[0]) and not first_node_already_exists:
                node1=node
                first_node_already_exists = True
            if(node.node_identifier == data[1] and not second_node_already_exists):
                node2=node
                second_node_already_exists = True

        if( not first_node_already_exists):
            node1 = Node(data[0])
            loaded_nodes.append(node1)
        if(not second_node_already_exists):
            node2 = Node(data[1])
            loaded_nodes.append(node2)
        edge= Edge(node1,node2,weight=int(data[2]))
        graph.add_edge(edge)
        read_line = connection_file.readline()
    connection_file.close()
    
    #Reading contents of city coordinates file
    city_coordinate_file= open('city coordinates data.txt')
    global city_cordinates
    city_cordinates={}
    read_line=city_coordinate_file.readline()
    while(read_line):
        read_line=read_line.split(',')
        city_cordinates[read_line[0]]=[float(read_line[1]),float(read_line[2])]
        read_line=city_coordinate_file.readline()
    city_coordinate_file.close()

city_cordinates=None
loaded_nodes=None
graph = Graph()
load_data(graph)
