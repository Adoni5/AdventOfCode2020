import re
from collections import defaultdict

from helpers.utils import get_puzzle_input
import numpy as np

test_input = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

rules, my_ticket, nearby_tickets = get_puzzle_input(16).split("\n\n")
# create the rules
prog = re.compile(r"([a-z A-Z]+): (\d+)-(\d+) or (\d+)-(\d+)")
prog_2 = re.compile(r"(\d+)-(\d+)")
a = prog.findall(rules)
b = prog_2.findall(rules)

my_ticket = list(map(int, my_ticket.split("\n")[1].split(",")))

rules_dict = {x[0]: [[int(x[1]), int(x[2])], [int(x[3]), int(x[4])]] for x in a}
error = 0
valid_tickets = set()
for ticket in nearby_tickets.splitlines()[1:]:
    ticket_valid = []
    for ticket_num in ticket.split(","):
        ticket_num = int(ticket_num)
        if not any(int(lower) <= ticket_num <= int(upper) for lower, upper in b):
            error += ticket_num
            ticket_valid.append(False)
        else:
            ticket_valid.append(True)
    if all(ticket_valid):
        valid_tickets.add(tuple(map(int, ticket.strip().split(","))))
arr = np.array(list(valid_tickets))
dicty = defaultdict(set)
for rule, ((lower1, upper1), (lower2, upper2)) in rules_dict.items():
    for i in range(arr.shape[1]):
        d = arr[:, i]
        if np.all((lower1 <= d) & (d <= upper1) | (lower2 <= d) & (d <= upper2)):
            dicty[rule].add(i)
order = {}
run = True
while run:
    for keys, cols in dicty.items():
        if len(cols) == 0:
            continue
        if len(cols) == 1:
            solved_columns = cols.pop()
            order[keys] = solved_columns
            for all_cols in dicty.values():
                all_cols.discard(solved_columns)
            test = [len(all_cols) for all_cols in dicty.values()]
            if not sum(test):
                run = False
answer_part_2 = []
for key, value in order.items():
    if key.startswith("departure"):
        print(value)
        answer_part_2.append(my_ticket[value])
print(f"Answer to part 2 is {np.prod(answer_part_2)}")
