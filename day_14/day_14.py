import itertools
from collections import defaultdict
import re
from helpers.utils import get_puzzle_input
test_input = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
mem = defaultdict(int)
prog = re.compile(r"([01X]{36}|\d+)")

for input_set in get_puzzle_input(14).split("mask = "):
	if not input_set:
		continue
	a = [prog.findall(line) for line in input_set.splitlines()]
	mask = a[0][0]
	for mem_address, numby in a[1:]:
		a = bin(int(mem_address))
		listy_p1 = []
		# listy_p2 = []
		c = ["0"] * (len(mask) - len(a[2:]))
		c = "".join(c)
		a = c + a[2:]
		# for ind, num in enumerate(a):
		# 	if mask[ind] != num and mask[ind] != "X":
		# 		listy_p1.append(mask[ind])
		# 	else:
		# 		listy_p1.append(num)

		listy_p2 = [mask[ind] if mask[ind] != num and mask[ind] != "0" else num for ind, num in enumerate(a)]
		# mem[mem_address] = int("".join(listy_p2), 2)
		bin_to_float = "".join(listy_p2)
		float_combos = set(itertools.product("01", repeat=bin_to_float.count("X")))
		for x in float_combos:
			temp = bin_to_float
			for y in x:
				temp = temp.replace("X", y, 1)
			mem[int(temp, 2)] = int(numby)
print(sum(mem.values()))
