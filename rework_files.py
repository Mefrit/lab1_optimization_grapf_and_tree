file_name = 'Fokin_128_1.txt'
# file_name = 'Taxicab_7.txt'
file_path = './answers/' + file_name
answer_path = './answers/Fokin_128_22.txt'
f = open(file_path, 'r')
w = open(answer_path, 'w')

while True:
    # считываем строку
    line = f.readline()
    # прерываем цикл, если строка пустая
    w.write('e ' + line )
    if not line:
        break
    # выводим строку
   

# f.write('c Вес дерева ' + str(total_weight) + ", число листьев = 2\n")
# f.write('p edge ' + str(len(points)) + ' ' + str(len(graph_edges)) + "\n")

# for edge in graph_edges:
#     f.write('e ' + str(edge.index1) + ' ' + str(edge.index2) + "\n")