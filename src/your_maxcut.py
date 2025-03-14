from src.graph import Graph, Edge

class YourMaxCut:
    def __init__(self, graph):
        self.__g: Graph = graph

        self.__has_run: bool = False

        self.__maxcut_value: float = 0.0
        self.__result: list[bool] = [False] * self.__g.number_nodes()

    def run(self):
        # TODO implement

        self.__has_run = True

    def has_run(self):
        return self.__has_run

    def maxcut_value(self):
        if self.__has_run:
            return self.__maxcut_value
        else:
            raise RuntimeError("Tried to access result before algorithm was run")

    def get_result(self):
        if self.__has_run:
            return self.__result
        else:
            raise RuntimeError("Tried to access result before algorithm was run")
