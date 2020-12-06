from helpers.utils import get_puzzle_input
from collections import Counter

# part 1
print(sum(len({*group.replace("\n", "")}) for group in get_puzzle_input(6).split("\n\n")))

# part 2
counter = 0
for group in get_puzzle_input(6).split("\n\n"):
    count = group.count("\n") + 1
    letters = Counter(group)
    for letter in {*group.replace("\n", "")}:
        if letters[letter] == count:
            counter += 1