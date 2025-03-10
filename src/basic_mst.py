from src.graph import Graph, Edge


class BasicTopsort:
    def __init__(self, graph):
        self.__g: Graph = graph

        self.__has_run: bool = False

    def run(self):
        mst_edges: list[Edge] = []

        edges: list[Edge] = []

        for e in self.__g.edge_iterator():
            edges.append(Edge(e.v, e.w, e.weight))

        edges.sort(key=lambda e: e.weight)

        print(edges)

        self.__has_run = True

    def has_run(self):
        return self.__has_run

    def get_result(self):
        if self.__has_run:
            return self.__result
        else:
            raise RuntimeError("Tried to access result before algorithm was run")
