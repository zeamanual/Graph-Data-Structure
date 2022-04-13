from asyncio import constants
from cProfile import label
import matplotlib.pyplot as plt
from search_algorithms import dfs,bfs,dfs_generic,get_huristic_value,dijkstra,a_star_search,add_random_node_to_graph
from graph_impl import graph, loaded_nodes,city_cordinates
import time
NAME_CONSTANTS = ['bfs','dfs','dijkstra','a star','bfs soln','dfs soln','dijkstra soln','a star soln']

#generate benchmark data by running the test ' benchmark_run_count ' times
def generate_benchmark_data(graph,benchmark_run_count=1):
    algorithms= { 'bfs':bfs, 'dfs':dfs, 'dijkstra':dijkstra, 'a start':a_star_search}
    total_time_data = { 'dfs':0, 'bfs':0, 'dijkstra':0, 'a star':0}
    total_solution_length={ 'dfs':0, 'bfs':0, 'dijkstra':0, 'a star':0}
    num=0
    for i in range(benchmark_run_count):
        for start_node in graph.graph.keys():
            for end_node in graph.graph.keys():
                start=time.time()
                path= bfs(graph,start_node,end_node)
                end=time.time()
                total_solution_length['bfs']+=len(path)
                total_time_data['bfs']+=(end-start)

                start=time.time()
                path=dfs(graph,start_node,end_node)
                end=time.time()
                total_solution_length['dfs']+=len(path)
                total_time_data['dfs']+=end-start

                start=time.time()
                path=dijkstra(graph,start_node,end_node)
                end=time.time()
                total_solution_length['dijkstra']+=len(path)
                total_time_data['dijkstra']+=end-start

                start=time.time()
                path=a_star_search(graph,start_node,end_node,city_cordinates)
                end=time.time()
                total_solution_length['a star']+=len(path)
                total_time_data['a star']+=end-start


    dfs_time=total_time_data['dfs']/(400*(benchmark_run_count))
    bfs_time=total_time_data['bfs']/(400*(benchmark_run_count))
    dijkstra_time=total_time_data['dijkstra']/(400*(benchmark_run_count))
    a_star_time=total_time_data['a star']/(400*(benchmark_run_count))

    dfs_average_soln_len=total_solution_length['dfs']/(400*(benchmark_run_count))
    bfs_average_soln_len=total_solution_length['bfs']/(400*(benchmark_run_count))
    dijkstra_average_soln_len=total_solution_length['dijkstra']/(400*(benchmark_run_count))
    a_star_average_soln_len=total_solution_length['a star']/(400*(benchmark_run_count))

    print('bfs time', bfs_time)
    print('dfs time', dfs_time)
    print('Dijkstra time  ',dijkstra_time)
    print('a search time ',a_star_time)
    print('')
    print('bfs average solution length', bfs_average_soln_len)
    print('dfs average solution length', dfs_average_soln_len)
    print('Dijkstra average solution length',dijkstra_average_soln_len)
    print('a search average solution length' ,a_star_average_soln_len)
    return { NAME_CONSTANTS[0]:bfs_time,NAME_CONSTANTS[1]:dfs_time,NAME_CONSTANTS[2]:dijkstra_time,NAME_CONSTANTS[3]:a_star_time,
    NAME_CONSTANTS[4]:bfs_average_soln_len,NAME_CONSTANTS[5]:dfs_average_soln_len,NAME_CONSTANTS[6]:dijkstra_average_soln_len,NAME_CONSTANTS[7]:a_star_average_soln_len}

data=[]

add_random_node_to_graph(graph,30,city_cordinates)
print("\n--------begining of 1 benchmark ( 250 nodes )-----\n")
result = generate_benchmark_data(graph,1)
data.append(result)
print("\n--------end of 1  benchmark----------\n")

add_random_node_to_graph(graph,50,city_cordinates)
print("\n--------begining of 2 benchmark ( 250 nodes )-----\n")
result = generate_benchmark_data(graph,1)
data.append(result)
print("\n--------end of 2 benchmark----------\n")

add_random_node_to_graph(graph,50,city_cordinates)
print("\n--------begining of 3  benchmark ( 250 nodes )-----\n")
result = generate_benchmark_data(graph,1)
data.append(result)
print("\n--------end of 3 benchmark----------\n")


add_random_node_to_graph(graph,50,city_cordinates)
print("\n--------begining of 4  benchmark ( 250 nodes )-----\n")
result = generate_benchmark_data(graph,1)
data.append(result)
print("\n--------end of 4 benchmark----------\n")



plot_data = [[],[],[],[]]

for row in data:
    for i in range(4):
        plot_data[i].append(row[NAME_CONSTANTS[i]])
counter = 0
for i in plot_data:
    plt.plot([50,100,150,200],i,label=NAME_CONSTANTS[counter])
    counter+=1
plt.xlabel("Number of Nodes")
plt.ylabel("Time in Second")
leg = plt.legend(loc='upper center')
plt.show()

plot_data = [[],[],[],[]]

for row in data:
    for i in range(4,8):
        plot_data[i-4].append(row[NAME_CONSTANTS[i]])

for i in plot_data:
    plt.plot([50,100,150,200],i,label=NAME_CONSTANTS[counter])
    counter+=1
leg = plt.legend(loc='upper center')
# plt.plot([30,40,50,60,70],plot_data[0])
# plt.plot([30,40,50,60,70],plot_data[1])
# plt.plot([30,40,50,60,70],plot_data[2])
# plt.plot([30,40,50,60,70],plot_data[3])


# plt.plot([50,100,150,200,250])
plt.xlabel("Number of Nodes")
plt.ylabel("Solution Length")
# # plt.plot([50,100,150,200,250],[6,8,1,3])
plt.show()