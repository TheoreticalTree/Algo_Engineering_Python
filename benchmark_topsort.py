from src.basic_topsort import *
from src.your_topsort import *
from src.io import *

import time


def run_benchmark_comparison(file: str) -> str:
    graph: Graph = Graph(edges=read_dimacs_format(file), directed=True)

    n: int = graph.number_nodes()
    m: int = graph.number_edges()

    start_time = time.time()
    basic_topsort: BasicTopsort = BasicTopsort(graph)
    basic_topsort.run()
    end_time = time.time()

    total_time_ms = (end_time - start_time) * 1000

    return file + "," + str(n) + "," + str(m) + "," + str(total_time_ms) + "\n"


def run_benchmark_yours(file: str) -> str:
    graph: Graph = Graph(edges=read_dimacs_format(file), directed=True)

    n: int = graph.number_nodes()
    m: int = graph.number_edges()

    start_time = time.time()
    your_topsort: YourTopsort = YourTopsort(graph)
    your_topsort.run()
    end_time = time.time()

    total_time_ms = (end_time - start_time) * 1000

    return file + "," + str(n) + "," + str(m) + "," + str(total_time_ms) + "\n"


if __name__ == "__main__":
    instances = [
        "ValidInstance1.txt",
        "ValidInstance2.txt",
        "ValidInstance3.txt",
        "ValidInstance4.txt",
        "ValidInstance5.txt",
    ]

    output: str = "Algorithm,Instance,N,M,runtime\n"

    for instance in instances:
        output += "Comparison," + run_benchmark_comparison("data/topsort/" + instance)

    for instance in instances:
        output += "Yours," + run_benchmark_yours("data/topsort/" + instance)

    print(output)

    with open("output_topsort.csv", "w") as file:
        file.write(output)
