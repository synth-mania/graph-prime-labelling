# Class for the individual Node in a Graph
# should not be used directly, as this representation is subject to change
# (subclasses of graph should be handled directly)
class Node:

    # Initializes the Node with it's value and neighbor list
    def __init__(self, neighbors: list["Node"] = None, value: int = None):
        self.neighbors = neighbors if neighbors is not None else []
        self.value = value
    
    def get_neighbors(self) -> list["Node"]:
        return self.neighbors

    # Literally just an alternate constructor that generates n Nodes
    # for convenience (because I'm lazy)
    @classmethod
    def nodes(cls, n: int) -> list["Node"]:
        return [cls() for _ in range(n)]

    # Link an arbitrary number of nodes.
    # This only defines a bidirectional link
    # Executing this on every node in a graph creates a complete graph
    # this is broken somehow right now, so MatrixGraph.__init__ directly accesses each node's neighbors attribute
    # @staticmethod
    # def link(*nodes: "Node"):
    #     for node_a in nodes:
    #         for node_b in nodes:
    #             if node_a is not node_b and node_b not in node_a.neighbors:
    #                 node_a.neighbors.append(node_b)

    def __str__(self):
        return f"Node {self.__hash__()}: {self.value}"


# This shouldn't be used directly to create Graph objects
# subclasses will create the structure of that specific kind of
# graph by linking their nodes, this class only provides shared methods.
class Graph:

    def __init__(self, *nodes: Node):
        self.nodes = list(nodes)

    def print(self):
        pass


# Defines a graph where the nodes, if they each occupied a space on a
# two dimensional tessellation of squares (a grid),
# are linked to their orthagonally adjacent neighbors
class MatrixGraph(Graph):
    
    # yeah, this is something better handled by numpy. I'll switch to that,
    # but this'll get the project off the ground
    @staticmethod
    def add_coords(*coords: list[int]):
        return [sum(x) for x in zip(*coords)]
    
    def is_valid_coordinate(self, coords: list[int]):
        for i in range(len(self.dim)):
            if coords[i] >= self.dim[i] or coords[i] < 0:
                return False
        return True
    
    # yields vectors that when added to a given coordinate, represent it's orthagonally adjacent neighbors
    def orth_adj_vect(self):
        for i in range(len(self.dim)):
            vect = [0 for _ in range(len(self.dim))]
            vect[i] = 1
            yield vect.copy()
            vect[i] = -1
            yield vect.copy()
    
    # yields every possible coordinate
    def possible_coords(self):
        vect = [0 for _ in range(len(self.dim))]

        while True:
            yield vect.copy()  # yield a copy to avoid mutations outside
            
            for i in range(len(vect)):
                if vect[i] < self.dim[i] - 1:
                    vect[i] += 1
                    for j in range(i):
                        vect[j] = 0
                    break
            else:
                # if we complete the loop without a break, all coordinates are exhausted
                return

    def linearize(self, coord: list[int]) -> int:
        index = 0
        stride = 1
        for i in range(len(self.dim)):
            index += coord[i] * stride
            stride *= self.dim[i]
        return index
    
    def get_node(self, coord: list[int]):
        return self.nodes[self.linearize(coord)]

    def __init__(self, *dim: int):
        self.dim = list(dim)
        volume = 1
        # noinspection PyStatementEffect
        [volume := volume * i for i in self.dim] # is there an easier way to do this? probably. is it shorter? possibly.
                                                 # but this uses the cool walrus 'assign and return' operator, so it's better.
        nodes = Node.nodes(volume)

        for coord in self.possible_coords():

            # a more opaque way of using a generator comprehension to get valid_neighbors in one line
            #    valid_neighbors = (self.add_coords(x, coord) for x in self.orth_adj_vect() if self.is_valid_coordinate(self.add_coords(x, coord)))

            possible_neighbors = [self.add_coords(coord, vect) for vect in self.orth_adj_vect()]
            valid_neighbors = filter(self.is_valid_coordinate, possible_neighbors)
            valid_nodes = [
                nodes[self.linearize(coord)] for coord in valid_neighbors
            ]
            
            # old broken line of code
            #    Node.link(nodes[self.linearize(coord)], *valid_nodes)

            # temporary bugfix, but it's messy. Ideally, I shouldn't be accessing Node fields directly
            nodes[self.linearize(coord)].neighbors = valid_nodes

        super().__init__(*nodes)

def print_2d_matrix_graph(graph: MatrixGraph):
    for i in range(graph.dim[1]):
        for j in range(graph.dim[0]):
            value = graph.get_node([j, i]).value
            value = "0" if value is None else str(value)
            print(value + " " * (5 - len(value)), end="")
        print()