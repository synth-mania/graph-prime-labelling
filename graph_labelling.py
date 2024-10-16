# Class for the individual Node in a Graph
class Node:

    # Initializes the Node with it's value and neighbor list
    def __init__(self, neighbors: list["Node"] = None, value: int = None):
        self.neighbors = neighbors if neighbors is not None else []
        self.value = value

    # Literally just an alternate constructor that generates n Nodes
    # for convenience (because I'm lazy)
    @classmethod
    def nodes(cls, n: int) -> list["Node"]:
        return [cls() for _ in range(n)]

    # Link an arbitrary number of nodes
    # This only defines a bidirectional link
    @staticmethod
    def link(*nodes: "Node"):
        for node_a in nodes:
            for node_b in nodes:
                if node_a is not node_b and node_b not in node_a.neighbors:
                    node_a.neighbors.append(node_b)

    def __str__(self):
        return f"Node {self.__hash__()}"


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

    @staticmethod
    def linearize(x, y, width) -> int:
        return x + y*width

    def __init__(self, m, n):
        self.size = [m, n]
        nodes = Node.nodes(m*n)

        for y in range(n):
            for x in range(m):

                # link to northward neighbor
                if y > 0:
                    Node.link(
                        nodes[MatrixGraph.linearize(x, y, m)],
                        nodes[MatrixGraph.linearize(x, y-1, m)]
                    )
                
                # link to eastward neighbor
                if x < (m-1):
                    Node.link(
                        nodes[MatrixGraph.linearize(x, y, m)],
                        nodes[MatrixGraph.linearize(x+1, y, m)]
                    )
                
                # link to southward neighbor
                if y < (n-1):
                    Node.link(
                        nodes[MatrixGraph.linearize(x, y, m)],
                        nodes[MatrixGraph.linearize(x, y+1, m)]
                    )
                
                # link to westward neighbor
                if x > 0:
                    Node.link(
                        nodes[MatrixGraph.linearize(x, y, m)],
                        nodes[MatrixGraph.linearize(x-1, y, m)]
                    )
        
        super().__init__(*nodes)
    
    def print(self):
        for i in range(self.size[1]):
            for j in range(self.size[0]):
                value = self.nodes[MatrixGraph.linearize(j, i, self.size[0])].value
                value = "0" if value is None else str(value)
                print(value + " " * (5 - len(value)), end="")
            print()


if __name__ == "__main__":

    # m = int(input("Input size (m x n)\nm: "))
    # n = int(input("n: "))

    test_graph = MatrixGraph(3, 3)
    test_graph.print()