# graph-prime-labelling

This repo is intended to be a place for me to throw any tools I write related to the problem of creating a prime labelling of graphs.

I'll add a description of each tool I add to this repository to this file.

## graph.py

Defines classes for representing undirected graphs.

The goal is to provide abstractions that will simplify future work on algorithms that generate graph prime labellings.

### graph.Node

Simply defines a class that represents each node or vertice in a graph

This should not be accessed directly for constructing or linking nodes, which is handled by Graph subclasses
but the Node attribute 'value' at this time can only be accessed directly.

### graph.Graph

An abstract class defining methods and attributes common to all graphs to allow easy extension of graph types.
Don't access this directly

### graph.MatrixGraph

A Graph subclass.
Defines an n-dimensional matrix graph (each node is linked to it's orthagonally adjacent neighbors)

```python
MatrixGraph(d1, d2, d3 ... dn)
```

To access individual nodes, use get_node(coordinate), where coordinate is a list of integers

```
test_graph = MatrixGraph(2, 4)
a_node = test_graph.get_node([1, 3])
```

This gets the node and the end of each dimension (bottom-right, if x increases to the right, and y increases downward)

```a_node.value``` refers to a_node's value. (useful for prime labelling purposes)

The other methods of MatrixGraph likely aren't going to be as useful, but here's a brief overview:

```test_graph.linearize(coord: list[int])``` take a coordinate as list of integers and returns the one-dimensional index of that node (indexed from 0)

```test_graph.possible_coords()``` is a generator that yields each valid coordinate in the graph starting at [0, 0, 0 ... n times] to the max of each dimension

```test_graph.is_valid_coordinate(coord: list[int])``` takes a coordinate as list of integers and returns a boolean value representing whether the coordinate is within the bounds of the matrix