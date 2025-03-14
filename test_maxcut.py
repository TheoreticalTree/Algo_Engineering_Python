import unittest

from src.your_maxcut import *
from src.basic_maxcut import *
from src.graph import *
from src.graph_generator import create_maxcut_instance

# Checks if the edges are identical disregarding direction
def isEdge(e: Edge, v: int, w:int, weight:float) -> bool:
    print(e.v, e.w, e.weight, v, w, weight)
    return e.weight == weight and ((e.v == v and e.w == w) or (e.v == w and e.w == v))

class MaxCutTest(unittest.TestCase):
    def test_MC_values_match_test(self):
        g: Graph = Graph(edges=create_maxcut_instance(100, 1000, 100.0, 42), directed=False, weighted=True)

        basic_maxcut: BasicMaxCut = BasicMaxCut(g, 10)
        basic_maxcut.run()

        result = basic_maxcut.get_result()

        true_mc_value: float = 0.0

        for e in g.edge_iterator():
            if result[e.v] != result[e.w]:
                true_mc_value += e.weight

        self.assertAlmostEqual(true_mc_value, basic_maxcut.maxcut_value())



if __name__ == "__main__":
    unittest.main()
