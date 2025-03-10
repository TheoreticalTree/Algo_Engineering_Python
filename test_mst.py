import unittest

from src.your_mst import *
from src.basic_mst import *
from src.graph import *

# Checks if the edges are identical disregarding direction
def isEdge(e: Edge, v: int, w:int, weight:float) -> bool:
    print(e.v, e.w, e.weight, v, w, weight)
    return e.weight == weight and ((e.v == v and e.w == w) or (e.v == w and e.w == v))

class MSTTest(unittest.TestCase):
    def test_line_test(self):
        g: Graph = Graph(n=3, directed=False, weighted=True)
        g.add_edge(Edge(2, 1, 2.0))
        g.add_edge(Edge(1, 0, 1.0))

        basic_mst: BasicMST = BasicMST(g)
        basic_mst.run()

        result = basic_mst.get_result()
        result.sort(key=lambda e: e.weight)

        self.assertEqual(basic_mst.mst_value(), 3.0)
        self.assertTrue(isEdge(result[0], 0, 1, 1.0))
        self.assertTrue(isEdge(result[1], 1, 2, 2.0))


    def test_circle_test(self):
        g: Graph = Graph(n=3, directed=False, weighted=True)
        g.add_edge(Edge(0, 1, 1.0))
        g.add_edge(Edge(1, 2, 3.5))
        g.add_edge(Edge(0, 2, -2.0))

        basic_mst: BasicMST = BasicMST(g)
        basic_mst.run()

        result = basic_mst.get_result()
        result.sort(key=lambda e: e.weight)

        self.assertEqual(basic_mst.mst_value(), -1.0)
        self.assertTrue(isEdge(result[0], 0, 2, -2.0))
        self.assertTrue(isEdge(result[1], 0, 1, 1.0))


    def test_larger_graph(self):
        g: Graph = Graph(n=7, directed=False, weighted=True)
        g.add_edge(Edge(0, 1, 1.0))
        g.add_edge(Edge(0, 2, 2.0))
        g.add_edge(Edge(1, 2, 3.0))
        g.add_edge(Edge(1, 3, 4.0))
        g.add_edge(Edge(1, 4, 5.0))
        g.add_edge(Edge(1, 5, 1.5))
        g.add_edge(Edge(2, 3, 1.8))
        g.add_edge(Edge(2, 4, 2.5))
        g.add_edge(Edge(2, 6, 4.0))
        g.add_edge(Edge(3, 6, 4.0))
        g.add_edge(Edge(4, 6, 5.0))
        g.add_edge(Edge(5, 6, 3.0))

        basic_mst: BasicMST = BasicMST(g)
        basic_mst.run()

        result = basic_mst.get_result()
        result.sort(key=lambda e: e.weight)

        print(result)

        self.assertEqual(basic_mst.mst_value(), 11.8)
        self.assertTrue(isEdge(result[0], 0, 1, 1.0))
        self.assertTrue(isEdge(result[1], 1, 5, 1.5))
        self.assertTrue(isEdge(result[2], 2, 3, 1.8))
        self.assertTrue(isEdge(result[3], 0, 2, 2.0))
        self.assertTrue(isEdge(result[4], 2, 4, 2.5))
        self.assertTrue(isEdge(result[5], 5, 6, 3.0))

if __name__ == "__main__":
    unittest.main()
