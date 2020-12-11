from helpers.utils import get_puzzle_input
test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

grid = {}
x = 0
y = 0
adjacency = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]
max_x = 0
max_y = 0
for position in get_puzzle_input(11):
    if position == "\n":
        y += 1
        x = 0
        continue
    grid[(x, y)] = position
    max_x = x
    x += 1
    max_y = y

run = True
z=0
while run:
    z+=1
    new_grid = {}
    for position, seat_info in grid.items():
        if seat_info == ".":
            new_grid[position] = grid[position]
            continue
        x, y = position
        adjacent_seats = {}
        # todo here is where we need to change the getting other seats code
        for dx, dy in adjacency:
            keep_looking = True
            i, j = 1, 1
            while keep_looking:
                neighbour = (x + dx * i, y + dy * j)
                if neighbour[0] > max_x or neighbour[1] > max_y or neighbour[0] < 0 or neighbour[1] < 0:
                    keep_looking = False
                    continue
                if neighbour[0] == max_x and x != max_x or neighbour[1] == max_y and y != max_y or neighbour[0] == 0 and x != 0 or neighbour[1] == 0 and y != 0:
                    adjacent_seats[neighbour] = grid[neighbour]
                    keep_looking = False
                elif grid[neighbour] == "L" or grid[neighbour] == "#":
                    adjacent_seats[neighbour] = grid[neighbour]
                    keep_looking = False
                i += 1
                j += 1
        occupied = list(adjacent_seats.values()).count("#")
        if not occupied and seat_info == "L":
            new_grid[position] = "#"
        elif occupied >= 5 and seat_info == "#":
            new_grid[position] = "L"
        else:
            new_grid[position] = grid[position]
    # if z == 3:
    if new_grid == grid:
        run = False
    grid = new_grid
print(f"{list(grid.values()).count('#')}")


# a = "".join(f"{i}\n" if ix % 10 == 0 and ix != 0 else i for ix, i in enumerate(list(grid.values())))
# print(a)
