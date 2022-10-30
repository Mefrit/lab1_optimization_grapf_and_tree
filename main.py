from math import fabs
from lib.connect import Connectivity
from lib.helpers import read_data, getEdges
# file_name = './data/Taxicab_64.txt'
file_name = 'Taxicab_5.txt'
# file_name = 'Taxicab_7.txt'
file_path = './data/' + file_name
answer_path = './answers/'+ file_name
# Идея алгоритма возьмём рандомную точку и будем присоединять минимальне ребра
# Каждое ребро связанно с каждым, оптимизация, если у точки вокруг нее веса рёбер хуже, чем у ее родителя. то делаем ход у родителя
f = open(file_path, 'r')

points = read_data(f)

graph_edges = getEdges(points)

graph_edges = sorted(graph_edges, key=lambda x: x.weight, reverse=False)

chosen_edges = []
def is_edges_connect(edge1, edge2):
    return edge1.point1 == edge2.point1 or edge1.point2 == edge2.point2

def addEdgeToConnectivity(cache_connectivy, edge):
# Добавит ребро в существующий связный компонент или создаст новый
    exist = False
    for connectivy in cache_connectivy:
        if exist != True:
            exist = connectivy.addEdge(edge)

    if exist == False:
        new_connectivy = Connectivity()
        new_connectivy.addEdge(edge)
        cache_connectivy.append(new_connectivy)
    return cache_connectivy


print('readed')
curent_weight = 1
cache_connectivy = []
for edge in graph_edges:
    # print(edge.getInfo())
    cache_connectivy = addEdgeToConnectivity(cache_connectivy, edge)

total_weight = 0
parent_connectivity = new_connectivy = Connectivity()
print('connect')
cache_connectivy = sorted(cache_connectivy, key=lambda x: x.calculateMetric(), reverse=False)
print('len cache_connectify')
print(len(cache_connectivy))
print('sorted')
for connectivy in cache_connectivy:
    # total_weight += connectivy.calculateWeight()
    # if len(parent_connectivity.deprecated_point) >= (len(points)-1):
    #     print("Finish")
    #     break;
    print(connectivy.getInfo(), connectivy.calculateMetric() )
    parent_connectivity.addConnectivity(connectivy)
    
parent_connectivity.deleteEqualEnds()
if abs(len(parent_connectivity.edges) - len(points)) != 1:
    print('deprecated_point',parent_connectivity.deprecated_point)


f = open(answer_path, 'w')

f.write('Вес дерева ' + str(parent_connectivity.calculateWeight()) + ", число листьев = 2\n")
f.write('edge ' + str(len(points)) + ' ' + str(len(parent_connectivity.edges)) + "\n")


for edge in parent_connectivity.edges:
    f.write(str(edge.index1) + ' ' + str(edge.index2)+ "\n")
print('total Weight ', total_weight)
print('deprecated_point ', len(parent_connectivity.deprecated_point), len(points))
print("parent_connectivity " +str(parent_connectivity.getInfo()))
# while True:
#     # Нужно пройтись по всем ребрам и добавить 
#     # их в компоненты связностиА потом соединить эти компоненты

