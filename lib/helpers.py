from random import randint
from .edge import Edge
from random import choice



def read_data(f):
    data = []
    i = 0
    while True:
        # считываем строку
        line = f .readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        # выводим строку
        if(i != 0):
            data.append(line.strip().split())
        i+=1
    return data

def read_data2(f):
    data = []
    i = 0
    while True:
        # считываем строку
        line = f .readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        # выводим строку
        if(i != 0):
            data.append(tuple([int(elem) for elem in line.strip().split()]))
        i+=1
    return data

def read_data(f):
    data = []
    i = 0
    while True:
        # считываем строку
        line = f .readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        # выводим строку
        if(i != 0):
            data.append(line.strip().split())
        i+=1
    return data

def getEdges(points):
    edge_index = 0
    graph_edges = []
    i = 0
    while i < len(points):
        j = i
        while j < len(points):
            if (i != j):
                if len(points[j]) > 0  and points[i]:
                    graph_edges.append(Edge(points[i],points[j], i + 1, j + 1,edge_index))
                    edge_index +=1
            j+=1
        i+=1
    return graph_edges

def getRandomPoint(start_index, points_len, deprecated_indexs):
    while True:
        new_index = randint(start_index, points_len)
        # print(new_index, "|| " ,start_index, points_len, " ||| ", deprecated_indexs)
        if new_index not in deprecated_indexs:
            break
    return new_index
    # return choice([i for i in range(start_index, points_len) if i not in [deprecated_indexs]])
def getRandomPoint2(cache):
    # cache
    # continue
    # вернет случайный индекс из массива
    
    if len(cache) == 1:
        return cache[0]
    
    return cache[randint(0, len(cache)-1)]
    # while True:
    #     new_index = randint(start_index, points_len)
    #     # print(new_index, "|| " ,start_index, points_len, " ||| ", deprecated_indexs)
    #     if new_index not in deprecated_indexs:
    #         break
    # return new_index
    # return choice([i for i in range(start_index, points_len) if i not in [deprecated_indexs]])
    
class Point:
    def __init__(self, point, index):
        self.point = point
        self.index = index
        self.neighbors = {}
        
    def add_neighbors(self, point):
        self.neighbors[point.index] = point
        
    def isFree(self):
        return len(self.neighbors) <= 2
    
    def getInfo(self):
        return 'Indx: ' + str(self.index) + " | " + str(self.point) + ' neigbors: ' + str([self.neighbors[neighbor].index for neighbor in self.neighbors]) + ""