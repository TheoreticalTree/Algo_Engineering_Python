from src.graph import Graph

class BasicTopsort:
    def __init__(self, graph):
        self.__g: Graph = graph

        self.__has_run: bool = False
        self.__k: int = 0
        self.__result: list[int] = []

    def run(self):
        n: int = self.__g.number_nodes()

        deg_in: list[int] = [0] * n
        at_deg_zero: list[int] = []

        for v in self.__g.node_iterator():
            deg_in[v] = self.__g.degree_in(v)
            if deg_in[v] == 0:
                at_deg_zero.append(v)

        next_round: list[int] = []
        vertices_done: int = 0
        result = [0] * n

        while len(at_deg_zero) != 0:
            self.__k += 1
            for v in at_deg_zero:
                for e in self.__g.outgoing_edges(v):
                    deg_in[e.w] -= 1
                    if deg_in[e.w] == 0:
                        next_round.append(e.w)
                result[v] = self.__k
                vertices_done += 1

            at_deg_zero, next_round = next_round, at_deg_zero
            next_round.clear()

        if vertices_done == n:
            self.__result = result
        else:
            self.__k = -1

        self.__has_run = True

    def has_run(self):
        return self.__has_run

    def get_result(self):
        if self.__has_run:
            return self.__result
        else:
            raise RuntimeError("Tried to access result before algorithm was run")

    def get_k(self):
        if self.__has_run:
            return self.__k
        else:
            raise RuntimeError("Tried to access result before algorithm was run")