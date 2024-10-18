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

    def set_graph(self, g: Graph):
        self.value["graph"] = g

    def set_unassigned(self, nums: list[int]):
        self.value["unassigned"] = nums

    def get_graph(self) -> Graph:
        return self.value["graph"]

    def get_unassigned(self) -> list[int]:
        return self.value["unassigned"].copy()


def permutate_tree_node(n: GraphTreeNode):
    graph = n.get_graph()

    # If the graph is empty
    # take the number with the most unique prime factors, and create a child graph node
    #
    if graph.is_empty():

        next_unassigned = n.get_unassigned()
        next_num = next_unassigned.pop() # .pop() retrieves the number with the most unique prime factors left

        for i in graph.node_index_by_degree():

            next_graph = deepcopy(graph)
            next_graph.get_node(i).set_value(next_num)

            child_node = n.grow_child()
            child_node.set_graph(next_graph)
            child_node.set_unassigned(next_unassigned.copy())


# This is a prime spot for optimization (lol)
def check_graph(g: Graph) -> bool:
    """
        Takes a Graph as input and returns a boolean value indicating
        whether the graph has a complete and valid prime labelling
    :param g:
    :return:
    """
    for i in range(g.size):
        this_node = g.get_node(i)

        for neighbor in this_node.neighbors:
            if not rel_prime(this_node.value, neighbor.value):
                return False
    return True


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
    # I want to sort the nums list by the smallest prime factor
    # i.e., the last numbers smallest prime factor is bigger than the smallest prime factor of any other number
    # unfortunately, because 1 is in the prime factor list for everything, it's not gonna be that simple.
    # I need to sort by the smallest prime factor except 1
    # nums = reversed(sorted(nums, key=lambda x: min(prime_factors(x))))
    nums_rank = sorted(nums, key=lambda x: len(set(prime_factors(x))))  # less -> more unique prime factors

    tree_root = tree.Node(root_graph)
    tree_root = GraphTreeNode(root_graph, nums_rank)


def main():
    print("input dimensions (m x n):")

    m = int(input("m: "))
    n = int(input("n: "))

    labelled_graph = get_prime_labelling(m, n)

    print("\n")

    if labelled_graph is None:
        print("No prime labelling was found")
    else:new_graph
        print_2d_matrix_graph(labelled_graph)


if __name__ == "__main__":
    main()