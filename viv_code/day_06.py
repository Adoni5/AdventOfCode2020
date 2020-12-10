from helpers.utils import get_puzzle_input
from collections import Counter
from string import ascii_lowercase
test_input = """abc

a
b
c

ab
ac

a
a
a
a

b"""
# groups = test_input.split("\n\n")
groups = get_puzzle_input(6, is_viv=True).split("\n\n")
total = 0
print(sum(len(set(group.replace("\n", ""))) for group in groups))

for group in groups:
    people = Counter(group)["\n"] + 1
    counts = Counter(group)
    for key, value in counts.items():
        if value == people:
            total += 1

# total = 0
# for group in groups:
#     setty = set(ascii_lowercase)
#     for person in group.splitlines():
#         setty = setty.intersection({*person})
#     total += len(setty)

print(total)