from src.graph import Edge, Graph
import random


def create_valid_topsort_instance(
    n: int, target_dge_number: int, seed: int
) -> list[Edge]:
    random.seed = seed

    max_edge_number = n * (n - 1) / 2

    edge_ratio: float = float(target_dge_number) / float(max_edge_number)

    vertex_alias: list[int] = list(range(0, n))
    random.shuffle(vertex_alias)

    edge_list: list[Edge] = []

    for v in range(n):
        for w in range(v + 1, n):
            chance: float = random.uniform(0, 1)
            if chance <= edge_ratio:
                edge_list.append(Edge(vertex_alias[v], vertex_alias[w], 1.0))

    return edge_list


def create_invalid_topsort_instance(
    n: int, target_dge_number: int, seed: int
) -> list[Edge]:
    random.seed = seed

    max_edge_number = n * (n - 1)

    edge_ratio: float = float(target_dge_number) / float(max_edge_number)

    vertex_alias: list[int] = list(range(0, n))
    random.shuffle(vertex_alias)

    edge_list: list[Edge] = []

    circle_size: int = random.randrange(n // 5, n // 2)

    for v in range(0, circle_size):
        edge_list.append(Edge(vertex_alias[v], vertex_alias[v + 1], 1.0))

    edge_list.append(Edge(vertex_alias[circle_size], vertex_alias[0], 1.0))

    for v in range(n):
        for w in range(n):
            if (v == w) or (abs(v - w) == 1 and w <= circle_size):
                continue

            chance: float = random.uniform(0, 1)
            if chance <= edge_ratio:
                edge_list.append(Edge(vertex_alias[v], vertex_alias[w], 1.0))

    return edge_list
