def read_graph(filename):
    pairs_list = []
    with open(filename, 'r') as file:
        for line in file:
            pair_str = line.strip().split()
            pair = (int(pair_str[0]), int(pair_str[1]))
            pairs_list.append(pair)
    return pairs_list


def generate_adjacency_matrix(n, edges):
    # Tworzenie macierzy zerowej
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    # Dodawanie krawędzi do macierzy
    for edge in edges:
        matrix[edge[0]-1][edge[1]-1] += 1
        matrix[edge[1]-1][edge[0]-1] += 1

    return matrix


def print_adjacency_matrix(n, matrix):
    for i in range(n):
        print('|', end=' ')
        for j in range(n):
            print(int(matrix[i][j]), end=' ')
        print('|')
    print()


def generate_incidence_matrix(n, edges):
    # Tworzenie macierzy zerowej
    matrix = [[0 for _ in range(len(edges))] for _ in range(n-1)]
    # Dodawanie krawędzi do macierzy
    for i, edge in enumerate(edges):
        matrix[edge[0]-1][i] = 1
        matrix[edge[1]-1][i] = 1
    return matrix


def print_incidence_matrix(v, e, matrix):
    for i in range(v):
        print('|', end=' ')
        for j in range(e):
            print(int(matrix[i][j]), end=' ')
        print('|')


def print_edges(edge_list):
    print('{', end="")
    for i in range(edge_list.__len__()-1):
        print(str(edge_list[i][0])+'-'+str(edge_list[i][1]), end=', ')
    print(str(edge_list[edge_list.__len__()-1][0])+'-'+str(edge_list[edge_list.__len__()-1][1]), end='}\n\n')


def generate_vertex_list(edge_list):
    vertex_list = list()
    for i in range(edge_list.__len__()):
        if edge_list[i][0] not in vertex_list:
            vertex_list.append(edge_list[i][0])
        if edge_list[i][1] not in vertex_list:
            vertex_list.append(edge_list[i][1])
    vertex_list.sort()
    return vertex_list


def print_vertex(edge_list):
    vertex_list = generate_vertex_list(edge_list)

    print('{', end='')
    for i in range(vertex_list.__len__()-1):
        print(vertex_list[i], end=', ')
    print(vertex_list[vertex_list.__len__()-1], end='}\n\n')


e_list = list()

e_list = read_graph('graf.txt')

v = e_list[0][0]
e = e_list[0][1]

e_list.pop(0)
print()
print("Liczba wierzcholkow grafu G wynosi "+str(v))
print("Zbior wierzcholkow V = ", end='')
print_vertex(e_list)
print("Liczba krawedzi grafu G wynosi "+str(e))
print("Zbior krawedzi E = ", end='')
print_edges(e_list)


somsiad_matrix = generate_adjacency_matrix(v, e_list)

print("Macierz sasiedztwa A =")
print_adjacency_matrix(v, somsiad_matrix)

print("Macierz incydencji M =")
imatrix = generate_incidence_matrix(e, e_list)
print_incidence_matrix(v, e, imatrix)

