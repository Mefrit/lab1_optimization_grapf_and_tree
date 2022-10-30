from unittest import result
from .edge import Edge

class Connectivity:
    'Класс, который будет хранить в себе связные рёбра'
    def __init__(self):
        self.edges = []
        self.deprecated_point = []

    def addEdge(self, edge):
        if len(self.edges) == 0:
            self.edges.append(edge)
            return True
        else:
            if self.checkNewEdgeByConnectEnd(edge, self.edges[-1]):
                return True

            if self.checkNewEdgeByConnectStart(edge, self.edges[0]):
                return True
        return False

    def checkNewEdgeByConnectStart(self, new_edge, parent):
        '''провекра на то, что новое ребро сможет войти в компоненту связности cyfxfkf'''
        if len(self.edges) == 0:
            return True
      
        res1, deprecated1 = self.checkPointOnEqual(parent.point1, new_edge.point1)
        res2, deprecated2 = self.checkPointOnEqual(parent.point2, new_edge.point2)
        res3, deprecated3 = self.checkPointOnEqual(parent.point1, new_edge.point2)
        res4, deprecated4 = self.checkPointOnEqual(parent.point2, new_edge.point1)
        # Проверка на то, что 1й элемент не содержит
        # res3 = self.checkPointOnEqual(self.edges[0].point1, new_edge.point1)
        # res4 = self.checkPointOnEqual(self.edges[0].point2, new_edge.point2)
        # print("insert "+ str(res1)+ " " + str(res2) + "  "+ str(res3)+ "  "+ str(res4)+" "+ str(len(self.edges)) + str(self.edges))
        # print('-------->>>>> ',parent.getPoints(), new_edge.getPoints() )
        if (res1 or res2 or res4 or res3) and not deprecated1 and not deprecated2 and not deprecated4 and not deprecated3:
            # print("insert "+ str(new_edge.getPoints()) + "  ---->>>> " + str(self.deprecated_point))
            # if res1: 
            if not self.sameDeprecatedPoint(parent.point1):
                self.deprecated_point.append(parent.point1)
                
            # else:
            if not self.sameDeprecatedPoint(parent.point2):
                self.deprecated_point.append(parent.point2)
            # self.deprecated_point.append(parent.point2)
            # self.deprecated_point.append(parent.point1)

            # self.deprecated_point.append(self.edges[0].point1)
            # self.deprecated_point.append(self.edges[0].point2)
            # tmp=self.edges.copy()
            self.edges.insert(0, new_edge)
            # print('insert;' + str(list(map(lambda edge: edge.getPoints(), tmp))) +" ++++ " + str(new_edge.getPoints()))
            # str(list(map(lambda edge: edge.getPoints(), self.edges))))
            # print("\n")
            return True
            
        return False
    def checkNewEdgeByConnectEnd(self, new_edge, parent):
        '''провекра на то, что новое ребро сможет войти в компоненту связности'''
        if len(self.edges) == 0:
              return True
        res1, deprecated1 = self.checkPointOnEqual(parent.point1, new_edge.point1)
        res2, deprecated2 = self.checkPointOnEqual(parent.point2, new_edge.point2)
        res3, deprecated3 = self.checkPointOnEqual(parent.point1, new_edge.point2)
        res4, deprecated4 = self.checkPointOnEqual(parent.point2, new_edge.point1)

        # res3 = self.checkPointOnEqual(self.edges[-1].point1, new_edge.point1)
        # res4 = self.checkPointOnEqual(self.edges[-1].point2, new_edge.point2)
        # print("append "+ str(res1)+ " " + str(res2) + "  "+ str(res3)+ "  "+ str(res4)+" "+ str(len(self.edges)))
      
        if (res1 or res2 or res4 or res3) and not deprecated1 and not deprecated2 and not deprecated4 and not deprecated3:

            if not self.sameDeprecatedPoint(parent.point1):
                self.deprecated_point.append(parent.point1)

            if not self.sameDeprecatedPoint(parent.point2):
                self.deprecated_point.append(parent.point2)

            self.edges.append(new_edge)
   
            return True
            
        return False    

    def sameDeprecatedPoint(self, new_point):
        result = False
        for point in  self.deprecated_point:
            if point[0] == new_point[0] and point[1] == new_point[1]:
                result = True;
                break
        return result

    def checkPointOnEqual(self, parent_point, new_point):
        # Провекра на то, что точка не входит в запрещенные
        deprecated = self.getDeprecated(new_point)
      
        return self.equal(parent_point, new_point), deprecated

    def getDeprecated(self, new_point):
        for point in self.deprecated_point:
            if(self.equal(point, new_point) == True):
                return True
        return False

    def equal(self, point1, point2):
        return point1[0] == point2[0] and point1[1] == point2[1]

    def getInfo(self):
        return list(map(lambda edge: edge.getPoints(), self.edges))

    def getInfo(self):
        return list(map(lambda edge: edge.getPoints(), self.edges))

    def getIndexes(self):
        return list(map(lambda edge: edge.getIndexs(), self.edges))

    def calculateWeight(self):
        total_weight = 0
        for edge in self.edges:
            total_weight += edge.weight
        return int(total_weight)

    def deleteEqualEnds(self):
        first = self.edges[0]
        last = self.edges[-1]
        res1, deprecated1 = self.checkPointOnEqual(first.point1, last.point1)
        res2, deprecated2 = self.checkPointOnEqual(first.point2, last.point2)
        res3, deprecated3 = self.checkPointOnEqual(first.point1, last.point2)
        res4, deprecated4 = self.checkPointOnEqual(first.point2, last.point1)

        if res1 or res2 or res3 or res4:
            if first.weight < last.weight:
                self.edges.pop(-1)
            else:
                self.edges.pop(0)
    def addConnectivity(self, new_connectivity):
        if len(self.edges) == 0:
            self.edges = new_connectivity.edges
            self.deprecated_point = new_connectivity.deprecated_point
            return
        for edge in new_connectivity.edges:
            if not self.getDeprecated(edge.point1) and not self.getDeprecated(edge.point1):
                self.addEdge(edge)

    def calculateMetric(self):
        return round (self.calculateWeight() / len(self.edges) -  0.7 * len(self.edges), 2)

    def addNewPoints(self, new_points):
        deprecated_point = []
        print(new_points, "\n\n\n")
        graph_edges = []
        print()
        first_last_point = self.edges[-1]
        for point in new_points:
            # graph_edges.append(Edge(points[i],points[j], i, j,edge_index))
            print(point,first_last_point)

            last = self.edges[-1]
            if not self.equal(first_last_point.point1, point['point']) and not self.equal(first_last_point.point2, point['point']):
                if not self.getDeprecated(last.point1):
                    edge = Edge( point['point'],last.point1,  point['index'],last.index1, 3)
                
                    self.edges.append(edge)
                else:
                    edge = Edge( point['point'],last.point2,  point['index'],last.index2, 3)
            
                    self.edges.append(edge)
            
                
        return

        # Нужно выбрать с каког оконца выгодней
# class Connectivity:
#     'Класс, который будет хранить в себе связные рёбра'
#     def __init__(self):
#         self.edges = {}

#     def addEdge(self, edge):
       
#         if self.checkNewEdgeByConnect(edge):
#             self.edges[edge.id] = edge
            
#             return True

#         return False

#     def checkNewEdgeByConnect(self, new_edge):
#         '''провекра на то, что новое ребро сможет войти в компоненту связности'''
#         if len(self.edges) == 0:
#             return True
#         result = False
#         print('leeen ', str(len(self.edges)) + str(self.edges[-1]))
#         for edge in self.edges:
#             if (self.checkPointOnEqual(self.edges[edge].point1, new_edge.point1) or 
#                 self.checkPointOnEqual(self.edges[edge].point2, new_edge.point2)):
#                 result = True
#         return result
    
#     def checkPointOnEqual(self, point1, point2):
#         return point1[0] == point2[0] and point1[1] == point2[1]

#     # def countLeaves(self):
#     #     count = 0
#     #     for edge in self.edges:

#     def getInfo(self):
#         return  str(self.edges)
