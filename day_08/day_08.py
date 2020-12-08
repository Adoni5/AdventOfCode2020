from helpers.utils import get_puzzle_input
test_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

class GameConsole:
    def __init__(self, input):
        self.boot_input = input.splitlines()
        self.index = 0
        self.accumulator = 0
        self.booting = True
        self.indexes = {0}
        self.changed_index = False
        self.changed_indices = []


    def jmp(self, amount):
        self.index += amount

    def nop(self, amount):
        self.index += 1
        pass

    def acc(self, amount):
        self.index += 1
        self.accumulator += amount

    def run(self):
        while self.booting:
            instruction = self.boot_input[self.index]
            instruction_type = instruction[:3]
            amount = int(instruction[3:])
            self.__getattribute__(instruction_type)(amount)
            if self.index not in self.indexes:
                self.indexes.add(self.index)
            else:
                self.booting = False
                print(f"Part 1 {self.accumulator}")

    def repair(self):
        self.booting = True
        self.refresh()
        while self.booting:
            try:
                instruction = self.boot_input[self.index]
            except IndexError:
                break
            instruction_type = instruction[:3]
            amount = int(instruction[3:])
            if instruction_type in {"nop", "jmp"} and not self.changed_index and not self.index in self.changed_indices:
                self.changed_index = True
                self.changed_indices.append(self.index)
            if self.changed_index and self.index == self.changed_indices[-1]:
                instruction_type = "nop" if instruction_type == "jmp" else "jmp"
            self.__getattribute__(instruction_type)(amount)
            if self.index not in self.indexes:
                self.indexes.add(self.index)
            else:
                self.refresh()
        print(f"Part 2: {self.accumulator}")

    def refresh(self):
        print(f"Refreshing and starting again!! \n\n\n")
        self.indexes = {0}
        self.changed_index = False
        self.accumulator = 0
        self.index = 0


gc = GameConsole(test_input)
gc.run()
assert gc.accumulator == 5
gc.repair()
assert gc.accumulator == 8

gc_full = GameConsole(get_puzzle_input(8))
gc_full.run()
gc_full.repair()
