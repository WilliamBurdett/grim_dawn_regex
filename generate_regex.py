from utils.character_management import add_skills_from_classes, extend_skills
from utils.damage_type_parsers import check_damage_source, calculate_damage_types, add_elemental


return_char = "\\n"
any_char = f"(.|{return_char})*"
level = "l: (9)(\d)"


def main():
    damage_type = "vitality"
    convert_from_types = []
    classes = [
        "necromancer",
        "occultist"
    ]
    skills = [
        "summon hellhound",
        "raise skeletons",
    ]
    damage_source = check_damage_source("pet")

    damage_types = calculate_damage_types(damage_type)

    add_elemental(convert_from_types)

    add_skills_from_classes(skills, classes)
    extend_skills(skills)

    if damage_source == "retaliation":
        print(f"/retaliation{any_char}({'|'.join(skills)}){any_char}{level}/")
        print(f"/retaliation{any_char}{level}/")
    elif damage_source == "player":
        print(f"/({'|'.join(damage_types)}) damage{return_char}{any_char}({'|'.join(skills)}){return_char}{any_char}{level}/")
        print(f"/({'|'.join(damage_types)}) damage{any_char}{level}/")
    elif damage_source == "pet":
        print(f"/({'|'.join(skills)}){return_char}{any_char}bonus to all pets{any_char}({'|'.join(damage_types)}) damage{return_char}{any_char}{level}/")
        print(f"/bonus to all pets{any_char}({'|'.join(damage_types)}) damage{return_char}{any_char}{level}")

    print(f"/(all skills{return_char})|({classes[0]}{any_char}{classes[1]})|({classes[1]}{any_char}{classes[0]})/")
    print(f"/({'|'.join(damage_types)}) damage{any_char}{level}/")
    if len(convert_from_types) > 0:
        print(f"/({'|'.join(convert_from_types)}) damage converted to {damage_type} damage{return_char}{any_char}{level}/")


if __name__ == '__main__':
    main()
