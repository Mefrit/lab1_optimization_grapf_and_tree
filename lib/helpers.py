from .edge import Edge


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
                    graph_edges.append(Edge(points[i],points[j],i, j,edge_index))
                    edge_index +=1
            j+=1
        i+=1
    return graph_edges