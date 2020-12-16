from helpers.utils import get_puzzle_input


def change_sign(number):
    """

    Parameters
    ----------
    number

    Returns
    -------

    """
    if number < 0:
        return number
    else:
        return -number

test_input = """F10
N3
F7
R90
F11"""

test_input_2 = """F37
E1
S5
R180
S1
F37
L180
F38"""

class Ship:
    def __init__(self):
        self.start = 0, 0
        self.directions = ("N", "E", "S", "W")
        self.directions_waypoint = (abs, abs, change_sign, change_sign)
        self.direction_index = 1
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1
        # self.waypoint_direction_index = [1, 0]

    def manhattan_distance(self):
        """Return the Manhattan distance between this point and another one."""
        x, y = self.start
        other_x, other_y = self.x, self.y
        print(abs(x - other_x) + abs(y - other_y))

    def turn(self, direction, degrees, part_1=False):
        rotations = int(degrees / 90)
        if part_1:
            index_change = -rotations if direction == "L" else rotations
            self.direction_index += index_change
        else:
            index_change = -rotations if direction == "L" else rotations
            index_x = 1 if self.waypoint_x > 0 else 3
            index_y = 0 if self.waypoint_y > 0 else 2
            index_x += index_change
            index_y += index_change
            if rotations % 2 == 0:
                print("even turns init")
                way_x = self.waypoint_x
                way_y = self.waypoint_y
                way_index_x = index_x
                way_index_y = index_y
            else:
                way_x = self.waypoint_y
                way_y = self.waypoint_x
                way_index_x = index_y
                way_index_y = index_x
            print(self.directions_waypoint[index_y % 4])
            temporary_x = self.directions_waypoint[way_index_x % 4](way_x)
            temporary_y = self.directions_waypoint[way_index_y % 4](way_y)
            self.waypoint_x = temporary_x
            self.waypoint_y = temporary_y

    def move(self, direction, amount):

        if direction == "F":
            self.x += (self.waypoint_x * amount)
            self.y += (self.waypoint_y * amount)
        if direction == "N":
            self.waypoint_y += amount
        elif direction == "S":
            self.waypoint_y -= amount
        elif direction == "E":
            self.waypoint_x += amount
        elif direction == "W":
            self.waypoint_x -= amount

    def instruction(self, instruction):
        for line in instruction.split("\n"):
            type = line[0]
            amount = int(line[1:])
            print(type, amount)
            print(f"Old waypoint at {self.waypoint_x}, {self.waypoint_y}")
            print(f"OG ship at {self.x}, {self.y}")
            if type in {"L", "R"}:
                self.turn(type, amount)
            else:
                self.move(type, amount)
            print(f"new waypoint {self.waypoint_x},{self.waypoint_y}")
            print(f"new x, y {self.x}, {self.y}")
            print("\n")
        print(self.x, self.y)
        self.manhattan_distance()


ship = Ship()
ship.instruction(get_puzzle_input(12))