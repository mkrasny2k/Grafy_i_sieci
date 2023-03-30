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


def print_edges(edge_list):
    print('{', end="")
    for i in range(edge_list.__len__()-1):
        print(str(edge_list[i][0])+'-'+str(edge_list[i][1]), end=', ')
    print(str(edge_list[edge_list.__len__()-1][0])+'-'+str(edge_list[edge_list.__len__()-1][1]), end='}\n\n')


def is_comlete(amatrix):
    for i in range(amatrix.__len__()):
        for j in range(amatrix.__len__()):
            if amatrix[i][j] == 0 and i != j:
                print("Graf nie jest grafem pełnym.")
                return False
    print("Graf jest grafem pełnym.")
    return True


def edges_needed_to_complete(amatrix):
    if is_comlete(amatrix) == False:
        ed_list = list()
        for i in range(amatrix.__len__()):
            for j in range(amatrix.__len__()):
                if amatrix[i][j] == 0 and i != j:
                    ed_list.append((i+1, j+1))
                    amatrix[i][j] = 1
                    amatrix[j][i] = 1
        print("Krawedzie dopelnienia grafu G: ", end='')
        print_edges(ed_list)


e_list = list()

e_list = read_graph('graf2.txt')

v = e_list[0][0]
e = e_list[0][1]

e_list.pop(0)
print()
am = generate_adjacency_matrix(v, e_list)


edges_needed_to_complete(am)