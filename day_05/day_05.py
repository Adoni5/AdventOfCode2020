# from collections import defaultdict
from helpers.utils import get_puzzle_input
import numpy as np
test_input = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""
#
# plane = defaultdict(dict)
#
#
# bf = ["b", "f"]
test_input = get_puzzle_input(5)
highest_id = 0
ids = []
for board_pass in test_input.split("\n"):
    rows = np.arange(0, 128)
    row_instructions = board_pass[:7]
    col_instructions = board_pass[7:]
    cols = np.arange(0,8)
    for row_section in row_instructions:
        limit = int(rows.size / 2)
        if row_section == "B":
            rows = rows[limit:]
        else:
            rows = rows[:limit]
    for col_section in col_instructions:
        limit = int(cols.size / 2)
        if col_section == "R":
            cols = cols[limit:]
        else:
            cols = cols[:limit]
    id = rows[0] * 8 + cols[0]

    if id > highest_id:
        highest_id = id
    ids.append(id)
