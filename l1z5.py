def read_graph(filename):
    pairs_list = []
    with open(filename, 'r') as file:
        for line in file:
            pair_str = line.strip().split()
            pair = (int(pair_str[0]), int(pair_str[1]))
            pairs_list.append(pair)
    return pairs_list


def generate_adjacency_list(edge_list):
    adjacency_list = {}
    for i, j in edge_list:
        if i not in adjacency_list:
            adjacency_list[i] = []
        if j not in adjacency_list:
            adjacency_list[j] = []
        if i != j:
            if j not in adjacency_list[i]:
                adjacency_list[i].append(j)
            if i not in adjacency_list[j]:
                adjacency_list[j].append(i)
    return adjacency_list


def print_adjacency_list(edge_list):
    adjacency_list=generate_adjacency_list(edge_list)
    print("Lista wierzcholkow grafu G:")
    for i in adjacency_list:
        print(str(i)+' -> '+str(adjacency_list[i]))


e_list = list()

e_list = read_graph('graf2.txt')

v = e_list[0][0]
e = e_list[0][1]

e_list.pop(0)

print_adjacency_list(e_list)