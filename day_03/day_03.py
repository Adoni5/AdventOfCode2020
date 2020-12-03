from helpers.utils import get_puzzle_input
import math
test_input = """..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"""


# Part 2
# right, down

tree_list = []
new_rules = [(1,1), (3,1), (5,1), (7,1), (1, 2)]


def get_tree_count(input, right, down):
    """
    Get the tree count for a given input and step size
    Parameters
    ----------
    input: str
        The puzzle input
    right: int
        number of places to move right
    down: int
        NUmber of rows to move down

    Returns
    -------

    """

    row_width = len(input.splitlines()[0])
    lines = input.splitlines()
    num_rows = len(input.splitlines())
    index = 0
    tree_count = 0
    for i in range(down, num_rows, down):
        index += right
        if index > row_width-1:
            index -= row_width
        if lines[i][index] == "#":
            tree_count += 1
    return tree_count


for right, down in new_rules:
    tree_list.append(get_tree_count(get_puzzle_input(3), right, down))

print(f"Part 1 {tree_list[1]}")
print(f"Part 2 {math.prod(tree_list)}")



