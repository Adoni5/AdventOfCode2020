from helpers.utils import get_puzzle_input
test_input = """1721
979
366
299
675
1456"""
reports = get_puzzle_input(1, is_viv=True).split("\n")
# reports = test_input.split("\n")
reports = list(map(int, reports))
for expense in reports:
    for expense_2 in reports:
        for expense_3 in reports:
            if int(expense_2) + int(expense) + int(expense_3) == 2020:
                print(int(expense_2) * int(expense) * int(expense_3))



