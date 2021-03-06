def add_elemental(input_type: list):
    for types in input_type:
        if types in ["cold", "fire", "lightning"]:
            input_type.append("elemental")


def calculate_damage_types(damage_types: list):
    all_types = ["all"]
    all_types.extend(damage_types)
    add_elemental(all_types)
    return all_types


def check_damage_source(damage_source):
    if damage_source not in ["player", "retaliation", "pet"]:
        print("Wrong damage source")
        exit(1)
    return damage_source
