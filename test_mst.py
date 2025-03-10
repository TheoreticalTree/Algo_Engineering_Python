import unittest

from src.your_topsort import *
from src.basic_topsort import *
from src.graph import *


class MSTTest(unittest.TestCase):
    def test_line_test(self):
        g: Graph = Graph(n=3, directed=False, weighted=True)
        g.add_edge(Edge(2, 1, 2.0))
        g.add_edge(Edge(1, 0, 1.0))

        basic_mst: BasicMST = BasicMST(g)
        basic_mst.run()

        self.assertEqual(basic_mst.mst_value(), 3.0)

    def test_circle_test(self):
        g: Graph = Graph(n=3, directed=True)
        g.add_edge(Edge(2, 1))
        g.add_edge(Edge(1, 0))
        g.add_edge(Edge(0, 2))

        your_topsort: YourTopsort = YourTopsort(g)
        your_topsort.run()

        self.assertEqual(your_topsort.get_k(), -1)
        self.assertEqual(len(your_topsort.get_result()), 0)

    def test_several_predecessors(self):
        g: Graph = Graph(n=7, directed=True)
        g.add_edge(Edge(0, 1))
        g.add_edge(Edge(0, 2))
        g.add_edge(Edge(1, 2))
        g.add_edge(Edge(1, 3))
        g.add_edge(Edge(1, 4))
        g.add_edge(Edge(1, 5))
        g.add_edge(Edge(2, 3))
        g.add_edge(Edge(2, 4))
        g.add_edge(Edge(2, 6))
        g.add_edge(Edge(3, 6))
        g.add_edge(Edge(5, 6))
        g.add_edge(Edge(6, 4))

        your_topsort: YourTopsort = YourTopsort(g)
        your_topsort.run()

        result: list[int] = your_topsort.get_result()

        self.assertEqual(your_topsort.get_k(), 6)
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 2)
        self.assertEqual(result[2], 3)
        self.assertEqual(result[3], 4)
        self.assertEqual(result[4], 6)
        self.assertEqual(result[5], 3)
        self.assertEqual(result[6], 5)


if __name__ == "__main__":
    unittest.main()
