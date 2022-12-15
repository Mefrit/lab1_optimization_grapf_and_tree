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
        self.x = point[0]
        self.y = point[1]
        self.index = index
        self.neighbors = {}
        
    def add_neighbors(self, point):

        if point != -1:
            self.neighbors[point.index] = point

    def neighborsLength(self):
        return len(self.neighbors)
    def isFree(self):
        return len(self.neighbors) <= 2
    
    def getInfo(self):
        return 'Indx: ' + str(self.index) + " | " + str(self.point) + ' neigbors: ' + str([self.neighbors[neighbor].index for neighbor in self.neighbors]) + ""

    def calculateWeight(self):
        weight = 0
        max_edge = 0
        for neighbor in self.neighbors:
            edge = Edge(self.point,  self.neighbors[neighbor].point, self.index + 1, self.neighbors[neighbor].index + 1, -1)
            weight += edge.weight
            if max_edge < edge.weight:
                max_edge = edge.weight
        return weight, max_edge

    def getEdjes(self, printed):
        output = []
        try:
            for neighbor in self.neighbors:
                print(neighbor,self.index)
                if self.neighbors[neighbor].index not in printed[self.index] and self.index  not in printed[ self.neighbors[neighbor].index]:
                    output .append( 'e ' + str(self.index + 1) + ' ' + str(self.neighbors[neighbor].index+ 1))
                    printed[self.index].append(self.neighbors[neighbor].index)

            return "\n".join(output), printed
        except Exception:
            return 'ERRORR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', printed
