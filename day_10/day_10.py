import operator
import numpy as np
from functools import reduce
from helpers.utils import get_puzzle_input

test_inout = """16
10
15
5
1
11
7
19
6
12
4"""
long_test_input = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
joltages = get_puzzle_input(10).splitlines()
joltages = list(map(int, joltages))
joltages.extend([0, max(joltages) + 3])
joltages.sort()
diffences = list(map(operator.sub, joltages[1:], joltages[:-1]))
arr = np.array(diffences)
print(f"Part 1: {np.flatnonzero(arr == 3).size * np.flatnonzero(arr == 1).size}")


# Part 2
consecutive_adapters = list(map(len, "".join("-" if x == 1 else "*" for x in diffences).split("*")))
addiitonal_combinations = [1, 1, 2, 4, 7]
print(f"Part 2: {reduce(operator.mul, [addiitonal_combinations[num_adapters] for num_adapters in consecutive_adapters])}")
