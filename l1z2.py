def read_graph(filename):
    pairs_list = []
    with open(filename, 'r') as file:
        for line in file:
            pair_str = line.strip().split()
            pair = (int(pair_str[0]), int(pair_str[1]))
            pairs_list.append(pair)
    return pairs_list


def vertex_degree(n, edge_list):
    vdeg = 0
    for i in range(edge_list.__len__()):
        if edge_list[i][0] == n:
            vdeg += 1
        if edge_list[i][1] == n:
            vdeg += 1
    return vdeg


def generate_vertex_list(edge_list):
    vertex_list = list()
    for i in range(edge_list.__len__()):
        if edge_list[i][0] not in vertex_list:
            vertex_list.append(edge_list[i][0])
        if edge_list[i][1] not in vertex_list:
            vertex_list.append(edge_list[i][1])
    vertex_list.sort()
    return vertex_list


def print_vertexes_degrees(vertex_list, edge_list):
    print("Stopnie wierzcholkow:")
    for vertex in vertex_list:
        print("deg("+str(vertex)+") = "+str(vertex_degree(vertex,edge_list)))
    print()


def generate_vertex_degree_sequence(vertex_list, edge_list):
    sequence = list()
    for vertex in vertex_list:
        sequence.append(vertex_degree(vertex, edge_list))
    sequence.sort()
    return sequence

def print_vertex_degree_sequence(vertex_list, edge_list):
    vds = generate_vertex_degree_sequence(vertex_list, edge_list)
    print("Ciąg stopni grafu G: ")
    for d in range(vds.__len__()-1):
        print(str(vds[d]), end=', ')
    print(str(vds[vds.__len__()-1]), end='\n\n')

e_list = list()

e_list = read_graph('graf.txt')

v = e_list[0][0]
e = e_list[0][1]

e_list.pop(0)
print()
print("Rząd grafu G wynosi "+str(v)+'\n')
print("Rozmiar grafu G wynosi "+str(e)+'\n')

v_list = generate_vertex_list(e_list)
print_vertexes_degrees(v_list, e_list)
print_vertex_degree_sequence(v_list, e_list)