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
count_searchers=2
points = read_data(f)
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
# print([1,2,3]- [2])
print(set_points)


def randomize():
    counter = 1
    for index_point in range(len(points)) :
        # Идея, мы для каждой точки выбираем 3 случайные вершины, и запоминаем их
        # Массив, для того, что бы он 1 и туже точку 2 раза подряд не взял
        broken_counter = False
        
        while set_points[index_point].isFree():
            counter+=1
            # print("\n\n")
            # print('curent ',set_points[index_point].getInfo(), set_points[index_point].isFree())
            
            # for point in set_points:
            #     print('|++++++++ > ',set_points[point].getInfo())
            for i in range(count_searchers):
                # Если точка свободна к отношениям вернём ее
                result = [set_points[item] for item in indexes_points if set_points[item].isFree() and  len(set_points[item].neighbors) != 3 and item != set_points[index_point].index]
                if len(result) == 0:
                    broken_counter = True
                    break
                else:
                    random_point = getRandomPoint2(result)
                print('result==>> ',result,random_point.getInfo())
            
            # Итак, выбрали случайную точку
            if set_points[index_point].isFree():
                set_points[index_point].add_neighbors(random_point)
                random_point.add_neighbors(set_points[index_point])
            print('set_points[index_point].getInfo()',counter, ' |> ', set_points[index_point].getInfo(), " ++> \n +", random_point.getInfo())
            if counter > 100 or broken_counter:
                broken_counter = True
                break
    if broken_counter:
        points_new = []
        for index_point in range(len(read_data(f))):

            points_new.append(Point(points[index_point], index_point))
            
            global_count_points[index_point] = 0
            indexes_points.append(index_point)
            set_points[index_point] = points_new[index_point]
        randomize()
randomize()
print(set_points)
for point in set_points:
    print('|===---===> ',set_points[point].getInfo())
  