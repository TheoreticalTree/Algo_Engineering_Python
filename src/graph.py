class Edge:
    def __init__(self, v: int, w: int, weight: float = 1.0):
        self.v = v
        self.w = w
        self.weight = weight

class Graph:
    def __init__(self, n: int = 0, edges: list[Edge] = None, directed: bool = False, weighted: bool = False):
        self.__directed: bool
        self.__weighted: bool
        self.__n: int = 0
        self.__m: int = 0

        self.__above_max_node_id: int

        # Stores currently dead vertices so holes in vertex ids can be fixed when new vertices are inserted
        self.__open_id_slots: list[int] = []

        # Stores outgoing edges by vertex and the position of where their other side is stored
        self.__edges_out: list[list[Edge]] = []
        self.__back_pos_out: list[list[int]] = []

        # Stores incoming edges by vertex and the position of where their other side is stored
        self.__edges_in: list[list[Edge]] = []
        self.__back_pos_in: list[list[int]] = []

        # stores of a vertex currently exists
        self.__alive: list[bool] = []

        if edges == None:
            self.__n = n
            self.__above_max_node_id = n
            self.__m = 0
            self.__directed = directed
            self.__weighted = weighted

            for i in range(n):
                self.__edges_out.append([])
                self.__back_pos_out.append([])
                self.__edges_in.append([])
                self.__back_pos_in.append([])

            self.__alive = [True] * n
        else:
            self.__above_max_node_id = 0

            for e in edges:
                self.__above_max_node_id = max(self.__above_max_node_id, max(e.v, e.w))

            self.__above_max_node_id += 1

            self.__n = self.__above_max_node_id
            self.__m = 0
            self.__directed = directed
            self.__weighted = weighted

            for i in range(self.__n):
                self.__edges_out.append([])
                self.__back_pos_out.append([])
                self.__edges_in.append([])
                self.__back_pos_in.append([])

            self.__alive = [True] * self.__n

            for e in edges:
                self.add_edge(e)


    def add_edge(self, e: Edge) -> None:
        self.__m += 1

        if (self.__directed):
            self.__edges_out[e.v].append(e)
            self.__edges_in[e.w].append(e)
            self.__back_pos_out[e.v].append(len(self.__edges_in[e.w]) - 1)
            self.__back_pos_in[e.w].append(len(self.__edges_out[e.v]) - 1)
        else:
            self.__edges_out[e.v].append(e)
            self.__edges_out[e.w].append(Edge(e.w, e.v, e.weight))
            self.__back_pos_out[e.v].append(len(self.__edges_out[e.w]) - 1)
            self.__back_pos_out[e.w].append(len(self.__edges_out[e.v]) - 1)

    def delete_edge(self, v: int, w: int) -> None:
        for i in range(len(self.__edges_out[v])):
            if self.__edges_out[v][i].w == w:
                self.__m -= 1

                if self.__directed:
                    back_pos = self.__back_pos_out[v][i]
                    self.__edges_out[v][i] = self.__edges_out[v][-1]
                    self.__back_pos_out[v][i] = self.__back_pos_out[v][-1]
                    self.__back_pos_in[self.__edges_out[v][i].w][self.__back_pos_out[v][i]] = i

                    self.__edges_in[w][back_pos] = self.__edges_in[w][-1]
                    self.__back_pos_in[w][back_pos] = self.__back_pos_in[w][-1]
                    self.__back_pos_out[self.__edges_in[w][back_pos].v][self.__back_pos_in[w][back_pos]] = back_pos

                    self.__edges_out[v].pop()
                    self.__back_pos_out[v].pop()
                    self.__edges_in[w].pop()
                    self.__back_pos_in[w].pop()
                else:
                    back_pos = self.__back_pos_out[v][i]
                    self.__edges_out[v][i] = self.__edges_out[v][-1]
                    self.__back_pos_out[v][i] = self.__back_pos_out[v][-1]
                    self.__back_pos_out[self.__edges_out[v][i].w][self.__back_pos_out[v][i]] = i

                    self.__edges_out[w][back_pos] = self.__edges_out[w][-1]
                    self.__back_pos_out[w][back_pos] = self.__back_pos_out[w][-1]
                    self.__back_pos_out[self.__edges_out[w][back_pos].w][self.__back_pos_out[w][back_pos]] = back_pos

                    self.__edges_out[v].pop()
                    self.__back_pos_out[v].pop()
                    self.__edges_out[w].pop()
                    self.__back_pos_out[w].pop()

                return

        raise Exception("Tried to delete an edge that does not exist")

    def has_edge(self, v: int, w: int) -> bool:
        if (v >= self.__above_max_node_id) or (w >= self.__above_max_node_id) or not self.__alive[v] or not self.__alive[w]:
            raise Exception("Checked if an edge exists for which at least one endpoint does not exist")

        for e in self.__edges_out[v]:
            if e.w == w:
                return True

        return False

    def add_vertex(self) -> int:
        self.__n += 1

        v: int = 0

        if len(self.__open_id_slots) > 0:
            v = self.__open_id_slots.pop()
            self.__alive[v] = True
            if v >= self.__above_max_node_id:
                self.__above_max_node_id = v + 1
        else:
            v = self.__above_max_node_id
            self.__edges_out.append([])
            self.__back_pos_out.append([])
            self.__alive.append(True)

            if self.__directed:
                self.__edges_in.append([])
                self.__back_pos_in.append([])

        return v

    def delete_vertex(self, v: int) -> None:
        if (v >= self.__above_max_node_id) or not self.__alive[v]:
            raise Exception("Tried to delete vertex that does not exist")

        while len(self.__edges_out[v]) > 0:
            self.delete_edge(v, self.__edges_out[v][0].w)

        if self.__directed:
            while len(self.__edges_in[v]) > 0:
                self.delete_edge(self.__edges_in[v][0].v, v)

        self.__alive[v] = False
        self.__n -= 1
        self.__open_id_slots.append(v)

        # Lower above max node id if necessary
        if v + 1 == self.__above_max_node_id:
            while not self.__alive[v] and v > 0:
                v -= 1

            if v == 0:
                if self.__alive[0]:
                    self.__above_max_node_id = 1
                else:
                    self.__above_max_node_id = 0
            else:
                self.__above_max_node_id = v + 1

    def has_vertex(self, v: int) -> bool:
        if v >= self.__above_max_node_id:
            return False

        return self.__alive[v]

    def edge_iterator(self):
        for v in range(self.__above_max_node_id):
            if self.__alive[v]:
                for e in self.__edges_out[v]:
                    if self.__directed:
                        yield e
                    elif e.v < e.w:
                        # ensures that we don't give the same edge twice
                        yield e

    def node_iterator(self):
        for v in range(self.__above_max_node_id):
            if self.__alive[v]:
                yield v

    def degree_in(self, v: int) -> int:
        return len(self.__edges_in[v])

    def degree_out(self, v: int) -> int:
        return len(self.__edges_out[v])

    def degree(self, v: int) -> int:
        if self.__directed:
            return len(self.__edges_out[v]) + len(self.__edges_in[v])
        else:
            return len(self.__edges_out[v])

    def incident_edges(self, v: int) -> list[Edge]:
        return self.__edges_out[v]

    def outgoing_edges(self, v: int) -> list[Edge]:
        return self.__edges_out[v]

    def incoming_edges(self, v: int) -> list[Edge]:
        return self.__edges_in[v]

    def number_nodes(self) -> int:
        return self.__n

    def number_edges(self) -> int:
        return self.__m
