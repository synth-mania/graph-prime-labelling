from graph import MatrixGraph, Graph, print_2d_matrix_graph, Node
from copy import deepcopy
import tree
from prime_tools import prime_factors, rel_prime


class GraphTreeNode(tree.Node):
    """
        extends 'tree.Node' to pack more data into 'tree.Node.value'

        Stores a Graph object and a list of the integers that have not been used to label the graph yet.

        new methods:
        get_graph() -> Graph
        get_unassigned() -> list[int]
    """
    def __init__(self, g: Graph = None, unassigned: list[int] = None, parent: "Node" = None):
        super().__init__({"graph": g, "unassigned": unassigned}, parent)

    def get_graph(self):
        return self.value["graph"]

    def get_unassigned(self):
        return self.value["unassigned"]

def free_adj_space(g: Graph) -> list[int] | None:
    """
        Gets a list of indexes of free nodes in a graph that are adjacent to non-free nodes

        If there are no free nodes adjacent to non-free nodes (if the graph is empty/full)
        returns None
    """

    unoccupied_i = (i for i in range(len(g.nodes)) if g.nodes[i].value is None or g.nodes[i].value == 0)
    occupied_adj_i = []

    for i in unoccupied_i:
        neighbor_values = (neighbor.value for neighbor in g.nodes[i].neighbors if neighbor.value is not None)

        for value in neighbor_values:
            if value > 0:
                occupied_adj_i.append(i)

    if not len(occupied_adj_i):
        return None
    return occupied_adj_i

# def permutate_tree_node(n: tree.Node, unassigned: list[int]):
#     if graph_is_empty(n.value):
#         for i in range(len(n.value.nodes)):


def get_prime_labelling(*dims: int) -> MatrixGraph | None:
    """
    Takes an arbitrary number of dimensions, and generates a MatrixGraph accordingly

    Attempts to find a valid prime labelling of the graph, and returns the resultant MatrixGraph object
    or None if no labelling was found.
    :param dims:
    :return:
    """
    root_graph = MatrixGraph(*dims)

    nums = [i + 1 for i in range(len(root_graph.nodes))]
    nodes_index_rank = sorted(range(len(root_graph.nodes)),
                              key=lambda x: len(root_graph.nodes[x].neighbors))  # less -> more neighbors
    nums_rank = sorted(nums, key=lambda x: len(set(prime_factors(x))))  # less -> more unique prime factors

    tree_root = tree.Node(root_graph)


def main():
    print("input dimensions (m x n):")

    m = int(input("m: "))
    n = int(input("n: "))

    labelled_graph = get_prime_labelling(m, n)

    if labelled_graph is None:
        print("No prime labelling was found")
    else:
        print_2d_matrix_graph(labelled_graph)


if __name__ == "__main__":
    main()
