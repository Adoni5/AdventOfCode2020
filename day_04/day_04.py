from helpers.utils import get_puzzle_input
from jsonschema import validate, exceptions

test_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

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
valid_count = 0
passport_strings = test_input.split("\n\n")
int_keys = {"byr", "iyr", "eyr"}
for passport in passport_strings:
    fields = {
        k: (int(v) if k in int_keys else v)
        for k, v in (e.split(":") for e in passport.split())
    }
    try:
        validate(instance=fields, schema=schema)
    except exceptions.ValidationError as err:
        continue
    valid_count += 1
print(f"Valid passports {valid_count}")
