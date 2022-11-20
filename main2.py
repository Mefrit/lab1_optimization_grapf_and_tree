import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import numpy as np
from lib.edge import Edge
from lib.helpers import read_data2, getEdges

file_name = 'Taxicab_4096.txt'
# file_name = 'Taxicab_7.txt'
file_path = './data/' + file_name
answer_path = './answers/Fokin_4096_test.txt'
# Идея алгоритма возьмём рандомную точку и будем присоединять минимальне ребра
# Каждое ребро связанно с каждым, оптимизация, если у точки вокруг нее веса рёбер хуже, чем у ее родителя. то делаем ход у родителя
f = open(file_path, 'r')

points = read_data2(f)
# print(points)
coords_list = points

additional_index = 512
# additional_index = 32
start_index = 0
cache_best_state = []
for i in range(int(round(len(points)/additional_index,0))):
    print('_________>>>> ',i, int(round(len(points)/additional_index,0)),start_index, start_index + additional_index)
    
    print(points[start_index : start_index + additional_index])
    graph_edges = getEdges(points[start_index:start_index + additional_index])
    # graph_edges = sorted(graph_edges, key=lambda x: x.weight, reverse=False)
    dist_list = []
    for edge in graph_edges:
        dist_list.append((edge.index1 - 1 , edge.index2 -1, edge.weight))
        # print(edge.index1, edge.index2, edge.weight)
    # Initialize fitness function object using coords_list

    fitness_coords = mlrose.TravellingSales(coords = points[start_index:start_index + additional_index])
    # print('dist_list',dist_list, len(graph_edges))
    if len(graph_edges) != 0 :
    # Initialize fitness function object using dist_list
        fitness_dists = mlrose.TravellingSales(distances=dist_list)


        problem_fit = mlrose.TSPOpt(length=additional_index, fitness_fn=fitness_coords,
                                    maximize=False)

        best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob=0.2,
        					      max_attempts = 100, random_state = 2)
        # best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state = 2)
        print("\n\n")
        print('The best state found is: ', best_state)

        print('The fitness at the best state is: ', best_fitness)
        
        points_result = []
        print('Lenn++ > ',len(best_state))
        start_index += additional_index
        cache_best_state.append(best_state)
        
# print(cache_best_state)
new_graph_edges = []
index_addition = 0
last_point = False
last_best_state = False

for best_state in cache_best_state:
    i1 = 1
    j1 = 0   
    # print('best_state ==>> ', best_state, index_addition, last_point)
    while i1 < len(best_state):
      
        if last_point != False:
            tmp = Edge(points[index_addition + best_state[i1]],last_point ,  index_addition + best_state[i1] + 1, last_best_state + 1, i)
            new_graph_edges.append(tmp)
            # print("\n\n\n",'11111111111111', tmp.getInfo())
            last_point = False
                      
        new_graph_edges.append(Edge(points[index_addition + best_state[i1]], 
                                    points[index_addition + best_state[j1]], 
                                    index_addition + best_state[i1] + 1,
                                    index_addition + best_state[j1] + 1, i))
        # print(points[index_addition + best_state[i1]],points[index_addition + best_state[j1]])
        if i1 == len(best_state) - 1:
            # print("\n -->>",points, len(best_state), index_addition + best_state[i1],points[index_addition + best_state[i1] - 1], points[index_addition + best_state[i1]], points[index_addition + best_state[i1-1]])
            last_point = points[index_addition + best_state[i1]]
            last_best_state = index_addition + best_state[i1]
            # print("\n", '!!!!!!!!!!!!!!!', i1, len(best_state) - 1, last_best_state, last_point, index_addition)
        i1 += 1
        j1 += 1
        
        total_weight = 0
    index_addition += additional_index
# print(graph_edges)
# i = 1
# j = 0
# graph_edges = []

# while i < len(best_state):
#     graph_edges.append(Edge(points[best_state[i]],points[best_state[j]], best_state[i] + 1, best_state[j] + 1, i))
#     i += 1
#     j += 1
# total_weight = 0
    

graph_edges = new_graph_edges
for edge in graph_edges:
    total_weight += edge.weight
    # print(edge.getInfo())
# print('total weight ==>> ', total_weight)
f = open(answer_path, 'w')
f.write('c Вес дерева ' + str(total_weight) + ", число листьев = 2\n")
f.write('p edge ' + str(len(points)) + ' ' + str(len(graph_edges)) + "\n")


for edge in graph_edges:
 
    f.write('e ' + str(edge.index1) + ' ' + str(edge.index2)+ "\n")

# print('deprecated_point ', len(parent_connectivity.edges), len(points))
# print("parent_connectivity " + str(parent_connectivity.getInfo()))