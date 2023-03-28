def read_pairs_from_file(filename):
    pairs_list = []
    with open(filename, 'r') as file:
        for line in file:
            pair_str = line.strip().split()
            pair = (int(pair_str[0]), int(pair_str[1]))
            pairs_list.append(pair)
    return pairs_list


def generate_adjacency_matrix(n, edges):
    # Tworzenie macierzy zerowej
    matrix = [[0 for _ in range(n-1)] for _ in range(n-1)]
    # Dodawanie krawędzi do macierzy
    for edge in edges:
        matrix[edge[0]-1][edge[1]-1] = 1
        matrix[edge[1]-1][edge[0]-1] = 1

    return matrix


def print_adjacency_matrix(n, matrix):
    for i in range(n):
        print('|', end=' ')
        for j in range(n):
            print(int(matrix[i][j]), end=' ')
        print('|')


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

e_list = list()

e_list=read_pairs_from_file('graf.txt')

v = e_list[0][0]
e = e_list[0][1]

e_list.pop(0)

print("Liczba wierzcholkow grafu G wynosi "+str(v))
print("Liczba krawedzi grafu G wynosi "+str(e))
print(e_list)

somsiad_matrix=generate_adjacency_matrix(e, e_list)

print_adjacency_matrix(v,somsiad_matrix)

print()
imatrix = generate_incidence_matrix(e, e_list)
print_incidence_matrix(v,e,imatrix)