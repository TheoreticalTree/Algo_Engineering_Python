from src.graph import Graph, Edge


class BasicMST:
    def __init__(self, graph):
        self.__g: Graph = graph

        self.__has_run: bool = False

        self.__mst_value: float = 0.0
        self.__result: list[Edge] = []

    def run(self):
        mst_edges: list[Edge] = []

        edges: list[Edge] = []

        for e in self.__g.edge_iterator():
            edges.append(Edge(e.v, e.w, e.weight))

        edges.sort(key=lambda e: e.weight)

        representatives: list[int] = list(range(self.__g.number_nodes()))
        components: list[list[int]] = []

        for v in self.__g.node_iterator():
            components.append([v])

        for e in edges:
            rep_v: int = representatives[e.v]
            rep_w: int = representatives[e.w]

            if rep_v != rep_w:
                mst_edges.append(e)
                self.__mst_value += e.weight

                if len(components[rep_v]) < len(components[rep_w]):
                    rep_v, rep_w = rep_w, rep_v

                for x in components[rep_w]:
                    representatives[x] = rep_v
                    components[rep_v].append(x)

                components[rep_w].clear()

        self.__result = mst_edges

        self.__has_run = True

    def has_run(self):
        return self.__has_run

    def mst_value(self):
        return self.__mst_value

    def get_result(self):
        if self.__has_run:
            return self.__result
        else:
            raise RuntimeError("Tried to access result before algorithm was run")
