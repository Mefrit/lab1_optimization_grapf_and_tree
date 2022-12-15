from math import fabs
from collections import Counter

from lib.edge import Edge
from lib.connect import Connectivity
from lib.helpers import read_data, getEdges, getRandomPoint, getRandomPoint2, Point
file_name = 'Taxicab_2048.txt'
# file_name = 'Taxicab_512.txt'
# file_name = 'Taxicab_7.txt'
global_index = 10

# Идея алгоритма возьмём рандомную точку и будем присоединять минимальне ребра
# Каждое ребро связанно с каждым, оптимизация, если у точки вокруг нее веса рёбер хуже, чем у ее родителя. то делаем ход у родителя
def globalAlg(global_index):
    global_index = global_index - 1 
    print('statr ----->>> ', global_index)
    file_path = './data/' + file_name
    answer_path = './answers_lab2/'+ str(global_index) + "_" + file_name
    f = open(file_path, 'r')
    count_searchers = 8
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

    global_count_points = {}
    indexes_points=[]
    set_points = {}

    for index_point in range(len(points)):
        points_new.append(Point(points[index_point], index_point))
        
        global_count_points[index_point] = 0
        indexes_points.append(index_point)
        set_points[index_point] = points_new[index_point]
    points = points_new
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
                if chose_point == -1:
                    is_error = True
                    break
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
    total_weight = 0

    cache_printed = {}
    max_edge = 0
    weght_edge = 0
    local_max_edge = 0
    is_error = False
    for point in set_points:
        cache_printed[set_points[point].index] = [] 
       
        if set_points[point].neighborsLength() != 3:
            is_error = True
            print("ERROR!!!!!!!!!!!")
            break
        weght_edge, local_max_edge = set_points[point].calculateWeight()
        total_weight += weght_edge
        if local_max_edge > max_edge:
            max_edge = local_max_edge

    if is_error or global_index > 0:
        if global_index > 0:
            globalAlg(global_index)
    else:
        print('weight: ', total_weight/2)
        f = open(answer_path, 'w')
        f.write('c Вес дерева ' + str(total_weight/2) + ", самое длинное ребро = " + str(max_edge) + "\n")
        f.write('p edge ' + str(len(points)) + "\n")

        for point in set_points:
            output, cache_printed = set_points[point].getEdjes(cache_printed)
            f.write(output +  "\n")
        print("\nGOOD")
globalAlg(global_index)