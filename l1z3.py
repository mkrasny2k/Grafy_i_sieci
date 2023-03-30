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

def is_simple(v, edge_list):
    counter = 0
    amatrix=generate_adjacency_matrix(v, edge_list)
    for i in range(v):
        for j in range(v):
            if amatrix[i][j] > 1:
                counter += 1

    if counter == 0:
        print("Graf G jest grafem prostym.")
        print()
    else:
        print("Graf G jest grafem ogólnym.")
        print()


e_list = list()

e_list = read_graph('graf2.txt')

v = e_list[0][0]
e = e_list[0][1]

e_list.pop(0)
print()
is_simple(v, e_list)