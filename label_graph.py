from graph import MatrixGraph, Graph


def prime_factors(x: int) -> list[int]:
    l = [x]

    def divides(a, b):
        return b // a == b / a

    last_cycle = False
    while not last_cycle:

        last_cycle = True

        for i in range(len(l)):
            for j in range(2, l[i]):
                if divides(j, l[i]):
                    last_cycle = False
                    l.append(j)
                    l[i] //= j

    l_filtered = list(
        x for x in l if x != 1  # I don't know why, but 1's randomly end up in here
    )

    l_filtered.append(1)

    return sorted(l_filtered)


def rel_prime(x: int, y: int):
    x_fact = set(prime_factors(x))
    y_fact = set(prime_factors(y))

    for i in x_fact:
        if i in y_fact and i != 1:
            return False

    return True

def generate_graph_permutations(g: Graph):
    occupied = (node for node in g.nodes if node.value is not None)
    occupied_adj = []

    for node in occupied:
        for neighbor in node.neighbors:
            if neighbor.value is None or neighbor.value == 0:
                occupied_adj.append(neighbor)

    free_nodes = set(occupied_adj)

    ### I've generated a list of the free nodes adjacent to filled nodes, but this function is not finished
    ### It must handle receiving an empty graph (select the node with most or least connections, I'd guess)
    ### I must also figure out how to tell this function which number to place in the empty spot in each permutation
    ### maybe it can just return a list of next node indexes?

print("input dimensions (m x n):")

m = int(input("m: "))
n = int(input("n: "))

the_graph = MatrixGraph(m, n)

nums = [i + 1 for i in range(m * n)]
nums_factored = [prime_factors(n) for n in nums]

nodes = the_graph.nodes
nodes_rank = sorted(nodes, key=lambda x: len(x.neighbors))
nodes_index_rank = sorted(range(len(the_graph.nodes)), key=lambda x: len(the_graph.nodes[x].neighbors))

nums_rank = sorted(nums, key=lambda x: len(set(prime_factors(x))))

for num in nums_rank:
    print(num)

graphs = []