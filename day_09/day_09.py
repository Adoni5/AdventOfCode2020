from collections import deque
from helpers.utils import get_puzzle_input
test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
def get_propertyless_number(input, preamble_len):
    """
    Get the first number that is not a sum of the immediately preceding preamble_len numbers
    Parameters
    ----------
    input: str
        The input to our puzzle
    preamble_len: int
        The length of the preceding numbers to check

    Returns
    -------
    int
        The first number that is not the sum of the preamble

    """
    input = list(map(int, input.splitlines()))
    preamble = deque(input[:preamble_len], maxlen=preamble_len)
    for number in input[preamble_len:]:
        if any((number - preambley in preamble for preambley in preamble)):
            preamble.append(number)
        else:
            return number

assert get_propertyless_number(test_input, 5) == 127

propertyless_number = get_propertyless_number(get_puzzle_input(9), 25)
print(f"Part 1: {propertyless_number}")

input = list(map(int, get_puzzle_input(9).splitlines()))
index = input.index(propertyless_number)
for i in range(1, index):
    for j in range(index):
        if sum(input[j:i+j]) == propertyless_number:
            print(f"Part 2: {min(input[j:i+j]) + max(input[j:i+j])}")
            break
