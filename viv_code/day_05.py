from helpers.utils import get_puzzle_input
test_input = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""
# passes = test_input.split("\n")
passes = get_puzzle_input(5, is_viv=True).split("\n")
all_id = []
for b_pass in passes:
    print(b_pass)
    row = b_pass[:7]
    column = b_pass[7:]
    plane = [i for i in range(128)]
    seats = [i for i in range(8)]
    for char in row:
        num_rows_to_keep = int(len(plane) / 2)
        if char == "B":
            plane = plane[num_rows_to_keep:]
        else:
            plane = plane[:num_rows_to_keep]
    for char in column:
        num_col_to_keep = int(len(seats) / 2)
        if char == "L":
            seats = seats[:num_col_to_keep]
        else:
            seats = seats[num_col_to_keep:]
    id = plane[0] * 8 + seats[0]
    all_id.append(id)
    print(f"Row: {plane[0]}, Column: {seats[0]}, ID: {id}")
print(max(all_id))
all_id.sort()
for index, id in enumerate(all_id):
    if all_id[index + 1] - id != 1:
        print(id + 1)
        break