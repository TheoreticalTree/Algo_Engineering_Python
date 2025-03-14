from src.basic_maxcut import BasicMaxCut
from src.your_maxcut import YourMaxCut
from src.io import *

import time


def run_benchmark_comparison(file: str, num_local_search: int) -> str:
    graph: Graph = Graph(edges=read_dimacs_format(file), directed=True)

    n: int = graph.number_nodes()
    m: int = graph.number_edges()

    start_time = time.time()
    basic_maxcut: BasicMaxCut = BasicMaxCut(graph, num_local_search)
    basic_maxcut.run()
    end_time = time.time()

    total_time_ms = (end_time - start_time) * 1000

    return file + "," + str(n) + "," + str(m) + "," + str(total_time_ms) + "," + str(basic_maxcut.maxcut_value()) + "\n"


def run_benchmark_yours(file: str) -> str:
    graph: Graph = Graph(edges=read_dimacs_format(file), directed=True)

    n: int = graph.number_nodes()
    m: int = graph.number_edges()

    start_time = time.time()
    your_maxcut: YourMaxCut = YourMaxCut(graph)
    your_maxcut.run()
    end_time = time.time()

    total_time_ms = (end_time - start_time) * 1000

    return file + "," + str(n) + "," + str(m) + "," + str(total_time_ms) + "," + str(your_maxcut.maxcut_value()) + "\n"


if __name__ == "__main__":
    instances = [
        "ValidInstance1.txt",
        "ValidInstance2.txt",
        "ValidInstance3.txt",
        "ValidInstance4.txt",
        "ValidInstance5.txt",
    ]

    output: str = "Algorithm,Instance,N,M,runtime,quality\n"

    for instance in instances:
        output += "Comparison[0]," + run_benchmark_comparison("data/maxcut/" + instance, 0)

    for instance in instances:
        output += "Comparison[1]," + run_benchmark_comparison("data/maxcut/" + instance, 1)

    for instance in instances:
        output += "Comparison[10]," + run_benchmark_comparison("data/maxcut/" + instance, 10)


    #for instance in instances:
    #    output += "Yours," + run_benchmark_yours("data/maxcut/" + instance)

    print(output)

    with open("output_maxcut.csv", "w") as file:
        file.write(output)
