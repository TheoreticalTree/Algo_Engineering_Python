# README

## Implement your own code
1) Implement your topsort code in ```src/your_topsort.py```
2) If you want to implement multiple algorithms solving the same problem remember updating the benchmacr scripts

## Generating Instances
**WARNING:** We assume that the base directory is the directory from which all code is executed. Many IDEs set the directory from which code is executed to *build* instead, which means the code doesn't find instance files where it expects them to be.
1) run ```python3 generate_instances.py``` to generate instances for Topological Sort (this may take a minute or two)

## Run tests
**WARNING:** We assume that the base directory is the directory from which all code is executed. Many IDEs set the directory from which code is executed to *build* instead, which means the code doesn't find instance files where it expects them to be.
1) Run ```python3 -m unittests TopsortTest``` to run the tests for topological sort
2) Run ```python3 -m unittests MSTTest``` to run the tests for topological sort

## Run Benchmarks
**WARNING:** We assume that the base directory is the directory from which all code is executed. Many IDEs set the directory from which code is executed to *build* instead, which means the code doesn't find instance files where it expects them to be.
1) Run ```python3 benchmark_topsort.py``` to run the benchmark for top sort and ```python3 benchmark_mst.py``` for mst
2) Run ```python3 plot_topsort.py``` to plot the output of benchmarking topsort and ```python3 plot_mst.py``` for mst (requires pandas and matplotlib)


