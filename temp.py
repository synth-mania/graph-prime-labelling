from graph import MatrixGraph
from graph import print_2d_matrix_graph



test_matrix = MatrixGraph(2, 2, 5, 6, 7)

print_2d_matrix_graph(test_matrix)

print()

for node in test_matrix.nodes:

    print(node.neighbors)