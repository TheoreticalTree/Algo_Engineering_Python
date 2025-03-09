from src.graph import *


def read_dimacs_format(file_name: str) -> list[Edge]:
    edge_list: list[Edge] = []

    with open(file_name, 'r') as file:
        next(file)

        for line in file:
            parts = line.split()

            edge_list.append(Edge(int(parts[0]), int(parts[1]), float(parts[2])))

    return edge_list

def write_edge_list_to_file(file_name: str, instance_name: str, edge_list: list[Edge]) -> None:
    with open(file_name, 'w') as file:
        file.write(instance_name + "\n")

        for e in edge_list:
            file.write(str(e.v) + " " + str(e.w) + " " + str(e.weight) + "\n")


