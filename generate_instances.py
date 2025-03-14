from src.graph_generator import *
from src.io import *
import os

import sys

def make_topsort_instances():
    folder_path = "data/topsort"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)

    for i in range(1, 6):
        print("Generating Topsort instances of size", 2000 * i)
        edge_list: list[Edge] = create_valid_topsort_instance(2000 * i, 20000 * i, 42)
        write_edge_list_to_file(
            folder_path + "/ValidInstance" + str(i) + ".txt",
            "ValidInstance" + str(i) + ".txt",
            edge_list,
        )
        edge_list: list[Edge] = create_invalid_topsort_instance(2000 * i, 20000 * i, 42)
        write_edge_list_to_file(
            folder_path + "/InvalidInstance" + str(i) + ".txt",
            "InvalidInstance" + str(i) + ".txt",
            edge_list,
        )

def make_mst_instances():
    folder_path = "data/mst"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)

    for i in range(1, 6):
        print("Generating MST instance of size", 2000 * i)
        edge_list: list[Edge] = create_valid_mst_instance(
            2000 * i, 20000 * i, 100.0, 42
        )
        write_edge_list_to_file(
            folder_path + "/ValidInstance" + str(i) + ".txt",
            "ValidInstance" + str(i) + ".txt",
            edge_list,
        )

def make_maxcut_instances():
    folder_path = "data/maxcut"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)

    for i in range(1, 6):
        print("Generating MaxCut instance of size", 2000 * i)
        edge_list: list[Edge] = create_maxcut_instance(
            2000 * i, 20000 * i, 100.0, 42
        )
        write_edge_list_to_file(
            folder_path + "/ValidInstance" + str(i) + ".txt",
            "ValidInstance" + str(i) + ".txt",
            edge_list,
        )

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if (sys.argv[1] == "topsort"):
            make_topsort_instances()
        elif sys.argv[1] == "mst":
            make_mst_instances()
        elif sys.argv[1] == "maxcut":
            make_maxcut_instances()
        else:
            print("Please select an option from topsort, mst or maxcut, or no option to make all instances")
    else:
        make_topsort_instances()
        make_mst_instances()
        make_maxcut_instances()

