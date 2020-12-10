from helpers.utils import get_puzzle_input
test_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
# all_data = test_input.split("\n")
all_data = get_puzzle_input(2, is_viv=True).split("\n")
total = 0
for password_data in all_data:
    bits = password_data.split(" ")
    pos_1, pos_2 = bits[0].split("-")
    pos_1, pos_2 = int(pos_1) - 1, int(pos_2) - 1
    char = bits[1][0]
    password = bits[2]
    if (password[pos_1] + password[pos_2]).count(char) == 1:
        print("Valid")
        total += 1
    else:
        print("Invalid")
print(total)