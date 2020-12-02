from helpers.utils import get_puzzle_input
from collections import Counter

# Test
test_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


def get_valid_passwords_count(puzzle_input):
    """
    Check the input string for invalid passwords
    Parameters
    ----------
    puzzle_input: str
        The puzzle input (new line delimited passwords and their associated rules)

    Returns
    -------
    int
        Number of valid passwords
    """
    counter_part_1 = 0
    counter_part_2 = 0
    for pwd in puzzle_input.split("\n"):
        bits = pwd.split(" ")
        lower_limit, upper_limit = bits[0].split("-")
        letter, pwd_letter_counts = bits[1][0], Counter(bits[2])
        if int(upper_limit) >= pwd_letter_counts[letter] >= int(lower_limit):
            counter_part_1 += 1
        part_two_password = Counter(f"{bits[2][int(lower_limit)-1]}{bits[2][int(upper_limit)-1]}")
        if part_two_password[letter] == 1:
            counter_part_2 += 1

    return counter_part_1, counter_part_2


# Test the function
assert get_valid_passwords_count(test_input) == (2, 1)

# Part 1
print(get_valid_passwords_count(get_puzzle_input(2)))

