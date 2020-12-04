from helpers.utils import get_puzzle_input
from jsonschema import validate, exceptions

schema = {
    "required": ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"],
    "properties": {
        "byr": {"type": "integer", "minimum": 1920, "maximum": 2002},
        "iyr": {"type": "integer", "minimum": 2010, "maximum": 2020},
        "eyr": {"type": "integer", "minimum": 2020, "maximum": 2030},
        "hgt": {
            "type": "string",
            "pattern": "^(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$",
        },
        "hcl": {"type": "string", "pattern": "^#[0-9a-f]{6}$"},
        "ecl": {"type": "string", "pattern": "^(blu|amb|brn|gry|grn|hzl|oth)$"},
        "pid": {"type": "string", "pattern": "^([0-9]{9})$"},
    },
}

test_input = get_puzzle_input(4)
part_1_valid_count = 0
part_2_valid_count = 0
passport_strings = test_input.split("\n\n")
int_keys = {"byr", "iyr", "eyr"}
for passport in passport_strings:
    fields = {
        k: (int(v) if k in int_keys else v)
        for k, v in (e.split(":") for e in passport.split())
    }
    part_1_valid_count += set(schema["required"]).issubset(set(fields.keys()))
    try:
        validate(instance=fields, schema=schema)
    except exceptions.ValidationError as err:
        continue
    part_2_valid_count += 1
print(f"Valid passports part 1: {part_1_valid_count}")
print(f"Valid passports part 2: {part_2_valid_count}")
