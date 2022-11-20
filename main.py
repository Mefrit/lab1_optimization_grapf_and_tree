from math import fabs
from collections import Counter

from lib.edge import Edge
from lib.connect import Connectivity
from lib.helpers import read_data, getEdges, getRandomPoint, getRandomPoint2, Point
# file_name = './data/Taxicab_64.txt'
file_name = 'Taxicab_cube8.txt'
# file_name = 'Taxicab_7.txt'
file_path = './data/' + file_name
answer_path = './answers/w_'+ file_name
# Идея алгоритма возьмём рандомную точку и будем присоединять минимальне ребра
# Каждое ребро связанно с каждым, оптимизация, если у точки вокруг нее веса рёбер хуже, чем у ее родителя. то делаем ход у родителя
f = open(file_path, 'r')
count_searchers= 100
files_points = read_data(f)
points = files_points
deprecated_indexs = []
# points = [Point((0,0), 0), Point((0,1), 1), Point((1,0),2), Point((1,1),3)]
len_points = len(points) - 1
# массив, где все подряд индексы точек, которые как то учавствуют в тусе
global_deprecated = []
# индексы точек, которые встречались уже 3 раза и их нельзя больше выбирать
random_deprecated = []

points_new=[]
print(points)
global_count_points = {}
indexes_points=[]
set_points = {}

for index_point in range(len(points)):
    points_new.append(Point(points[index_point], index_point))
    
    global_count_points[index_point] = 0
    indexes_points.append(index_point)
    set_points[index_point] = points_new[index_point]
points = points_new
print('points ==> ',points)
localpoints = []
globalpoints = []

def randomize(points,set_points,indexes_points):
    counter = 1
    for index_point in range(len(points)) :
        # Идея, мы для каждой точки выбираем 3 случайные вершины, и запоминаем их
        # Массив, для того, что бы он 1 и туже точку 2 раза подряд не взял
        broken_counter = False
        
        while set_points[index_point].isFree():
            counter+=1
            min_weight = 1000000000
            chose_point = -1
            for i in range(count_searchers):
                # Если точка свободна к отношениям вернём ее
                result = [set_points[item] for item in indexes_points if set_points[item].isFree() and item != set_points[index_point].index]
               
                if len(result) == 0:
                    broken_counter = True
                    break
                else:
                    random_point = getRandomPoint2(result)
                
                test_edge = Edge(set_points[index_point].point ,random_point.point, set_points[index_point].index, random_point.index,-1)
                if test_edge.weight < min_weight:
                    min_weight = test_edge.weight
                    chose_point = random_point

            # Итак, выбрали случайную точку
            if set_points[index_point].isFree():
                set_points[index_point].add_neighbors(chose_point)
                chose_point.add_neighbors(set_points[index_point])

            if counter > 1000 or broken_counter:
                broken_counter = True
                break

    if broken_counter:
        points_new = []
        points1 = files_points
        indexes_points= []
        set_points={}
        for index_point in range(len(points1)):

            points_new.append(Point(points1[index_point], index_point))
            
            global_count_points[index_point] = 0
            indexes_points.append(index_point)
            set_points[index_point] = points_new[index_point]
        randomize(points, set_points,indexes_points)

randomize(points, set_points, indexes_points)

print(set_points)
for point in set_points:
    print('|===---===> ',set_points[point].getInfo())
    
  