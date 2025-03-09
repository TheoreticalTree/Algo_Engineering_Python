from src.graph_generator import *
from src.io import *
import os

if __name__ == "__main__":
    folder_path = 'data/topsort'

    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)

    for i in range(1, 6):
        print("Generating Topsort instances of size", 1000 * i)
        edge_list: list[Edge] = create_valid_topsort_instance(1000 * i, 10000 * i, 42)
        write_edge_list_to_file(folder_path + "/ValidInstance" + str(i) + ".txt", "ValidInstance" + str(i) + ".txt", edge_list)
        edge_list: list[Edge] = create_invalid_topsort_instance(1000 * i, 10000 * i, 42)
        write_edge_list_to_file(folder_path + "/InvalidInstance" + str(i) + ".txt", "InvalidInstance" + str(i) + ".txt", edge_list)