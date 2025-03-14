from src.graph import Graph, Edge

class BasicMaxCut:
    def __init__(self, graph, num_local_search_rounds: int = 0):
        self.__g: Graph = graph
        self.__num_local_search_rounds = num_local_search_rounds

        self.__has_run: bool = False

        self.__maxcut_value: float = 0.0
        self.__result: list[bool] = [False] * self.__g.number_nodes()

    def run(self):
        n: int = self.__g.number_nodes()

        gain_from_A: list[float] = [0.0] * n

        for v in self.__g.node_iterator():
            if gain_from_A[v] > 0:
                self.__result[v] = True

                for e in self.__g.incident_edges(v):
                    gain_from_A[e.w] -= e.weight
            else:
                for e in self.__g.incident_edges(v):
                    gain_from_A[e.w] += e.weight

        for e in self.__g.edge_iterator():
            if self.__result[e.v] != self.__result[e.w]:
                self.__maxcut_value += e.weight

        improvement_occured:bool = False

        for i in range(self.__num_local_search_rounds):
            improvement_occured = False

            for v in self.__g.node_iterator():
                print(gain_from_A[v], self.__result[v])

                # Check if flipping the solution will yield an improvement
                if (gain_from_A[v] != 0.0) and (self.__result[v] != (gain_from_A[v] > 0.0)):
                    print("Local Search Improvement occured")

                    improvement_occured = True

                    self.__result[v] = not self.__result[v]

                    if self.__result[v]:
                        assert (gain_from_A[v] > 0.0)

                        self.__maxcut_value += gain_from_A[v]

                        for e in self.__g.outgoing_edges(v):
                            gain_from_A[e.w] -= 2.0 * e.weight
                    else:
                        assert (gain_from_A[v] < 0.0)

                        self.__maxcut_value -= gain_from_A[v]

                        for e in self.__g.outgoing_edges(v):
                            gain_from_A[e.w] += 2.0 * e.weight

            if not improvement_occured:
                break

        self.__has_run = True

    def has_run(self):
        return self.__has_run

    def maxcut_value(self):
        return self.__maxcut_value

    def get_result(self):
        if self.__has_run:
            return self.__result
        else:
            raise RuntimeError("Tried to access result before algorithm was run")
