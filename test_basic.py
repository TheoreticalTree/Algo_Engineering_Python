import unittest

from src.graph import *

class MyTestCase(unittest.TestCase):
    def test_basic_directed_graph(self):
        g: Graph = Graph(n=5, directed=True, weighted=True)

        g.add_edge(Edge(0, 1, 3.0))
        g.add_edge(Edge(1, 0, -1.5))
        g.add_edge(Edge(4, 1, 0.3))
        g.add_edge(Edge(0, 3, 1.2))

        for v in g.node_iterator():
            print(f"Has node {v}")

        for e in g.edge_iterator():
            print(f"Has edge from {e.v} to {e.w} with weight {e.weight}")

        g.delete_vertex(3)
        g.delete_edge(0, 1)

        for v in g.node_iterator():
            print(f"Has node {v}")

        for e in g.edge_iterator():
            print(f"Has edge from {e.v} to {e.w} with weight {e.weight}")


if __name__ == '__main__':
    unittest.main()
