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


def create_valid_mst_instance(
    n: int, target_edge_number: int, maximum_weight: float, seed: int
):
    max_edge_number = n * (n - 1) / 2

    edge_ratio: float = float(target_edge_number) / float(max_edge_number)

    vertex_alias: list[int] = list(range(0, n))
    random.shuffle(vertex_alias)

    edge_list: list[Edge] = []

    representatives: list[int] = list(range(0, n))
    components: list[list[int]] = []
    for v in range(n):
        components.append([v])

    for v in range(n):
        for w in range(v + 1, n):
            chance: float = random.uniform(0, 1)
            if chance <= edge_ratio:
                edge_list.append(
                    Edge(
                        vertex_alias[v],
                        vertex_alias[w],
                        random.uniform(-maximum_weight, maximum_weight),
                    )
                )

                rep_v: int = representatives[v]
                rep_w: int = representatives[w]

                if rep_v != rep_w:
                    if len(components[rep_v]) < len(components[rep_w]):
                        rep_v, rep_w = rep_w, rep_v

                    for x in components[rep_w]:
                        representatives[x] = rep_v
                        components[rep_v].append(x)

                    components[rep_w].clear()

    for v in range(1, n):
        if components[0] != components[v]:
            edge_list.append(
                Edge(
                    vertex_alias[0],
                    vertex_alias[v],
                    random.uniform(-maximum_weight, maximum_weight),
                )
            )

            rep_v: int = representatives[v]
            rep_w: int = representatives[0]

            if rep_v != rep_w:
                if len(components[rep_v]) < len(components[rep_w]):
                    rep_v, rep_w = rep_w, rep_v

                for x in components[rep_w]:
                    representatives[x] = rep_v
                    components[rep_v].append(x)

                components[rep_w].clear()

    return edge_list

def create_maxcut_instance(
    n: int, target_edge_number: int, maximum_weight: float, seed: int
):
    max_edge_number = n * (n - 1) / 2

    edge_ratio: float = float(target_edge_number) / float(max_edge_number)

    edge_list: list[Edge] = []

    for v in range(n):
        for w in range(v + 1, n):
            chance: float = random.uniform(0, 1)
            if chance <= edge_ratio:
                edge_list.append(
                    Edge(
                        v,
                        w,
                        random.uniform(-maximum_weight, maximum_weight),
                    )
                )

    return edge_list