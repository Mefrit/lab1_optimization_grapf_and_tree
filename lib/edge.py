
class Edge:
    'Это класс Edge'
    def __init__(self, point1, point2, index1, index2, edge_index):
        self.point1 = point1
        self.point2 = point2
        self.index1 = index1
        self.index2 = index2
        self.id = edge_index
        self.weight = self.calculate_distance(point1[0], point1[1], point2[0],  point2[1])

    def getInfo(self):
        return str(self.id) + ' -weight: ' + str(self.weight) + ' p1 ' + str(self.point1) + ' p2 ' + str(self.point2)  + ' i1: ' + str(self.index1) + ' i2: ' + str(self.index2)
    def getIndexs(self):
        return 'e ' +  str(self.index1) + ' ' + str(self.index2)
    def getPoints(self):
        return '[' + str(self.point1) + ' ' + str(self.point2)+ "]"
    def calculate_distance(self, x, y, a, b):
        # 𝑥 − 𝑎| + |𝑦 − 𝑏|.
        return abs(int(x) - int(a)) + abs(int(y) - int(b))

        


