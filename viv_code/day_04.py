count = 0
for passport in puzzle_input_text.split("\n\n"):
    key_value_dict = {}
    passport_info = passport.split()
    for passport_info_bit in passport_info:
        key, value = passport_info_bit.split(":")
        if key in ["byr", "eyr", "iyr"]:
            value = int(value)
        key_value_dict[key] = value
        print(key_value_dict)
    if len(key_value_dict) == 8:
        count +=1
    elif len(key_value_dict) == 7 and "cid" not in key_value_dict:
        count +=1
    if all([
    
    key_value_dict.get("byr", 0) >= 1920 and key_value_dict.get("byr", 0) <= 2002,
    key_value_dict.get("iyr", 0) >= 2010 and key_value_dict.get("iyr", 0) <= 2020,
    key_value_dict.get("eyr", 0) >= 2020 and key_value_dict.get("eyr", 0) <= 2030,
    check_valid_hgt(key_value_dict.get("hgt", "acbcgadbdwa"))]):
        print("valid")
    
print(count)

