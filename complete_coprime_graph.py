from graph import Graph, Node
from prime_tools import coprime

class CompleteCoprimeGraph(Graph):
    def __init__(self, n: int):

        # create n nodes
        nodes = Node.nodes(n)

        # initialize Graph with nodes
        super().__init__(*nodes)

        # label each node
        for i in range(self.size):
            self.get_node(i).set_value(i+1)

        # link every node to every other node it with which it is coprime
        for i in range(self.size - 1):
            for j in range(i + 1, self.size):
                # print(f"Checking {i+1}, {j+1}")
                if coprime(i+1, j+1):

                    self.get_node(i).neighbors.append(
                        self.get_node(j)
                    )

                    self.get_node(j).neighbors.append(
                        self.get_node(i)
                    )


if __name__ == "__main__":
    print("complete coprime graph demonstration\n")
    n = int(input("How many nodes in the graph? : "))
    demo_graph = CompleteCoprimeGraph(n)

    for node in demo_graph.nodes:

        print(f"{node.value}: ", " ".join(str(x) for x in (i.value for i in node.neighbors)))