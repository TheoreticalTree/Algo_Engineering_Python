from src.graph import Graph

class BasicTopsort:
    def __init__(self, graph):
        __g = graph

    def run(self):
        # TODO: Implement the algorithm
        print("You should implement the algorithm")

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

    __g: Graph

    __has_run: bool = False
