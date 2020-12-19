from utils.character_management import add_skills_from_classes, extend_skills
from utils.damage_type_parsers import (
    check_damage_source,
    calculate_damage_types,
    add_elemental,
)
from utils.output_messages import retaliation_messages, player_messages, pet_messages, return_char, \
    add_both_skills_message, add_convert_types_message


def main():
    damage_types_list = ["physical"]
    convert_from_types_list = []
    classes_list = [
        "soldier",
        "oathkeeper"
    ]
    skills_list = [
        "blitz",
        "shattering smash",
        "oleron's rage",
    ]
    damage_source = check_damage_source("player")

    damage_types_list = calculate_damage_types(damage_types_list)

    add_elemental(convert_from_types_list)

    add_skills_from_classes(skills_list, classes_list)
    extend_skills(skills_list)
    skills_list.extend(classes_list)

    skills = "|".join(skills_list)
    damage_types = "|".join(damage_types_list)
    convert_from_types = "|".join(convert_from_types_list)

    messages = {"retaliation": retaliation_messages, "player": player_messages, "pet": pet_messages}

    output = messages[damage_source](skills, damage_types)
    add_both_skills_message(output, classes_list)
    add_convert_types_message(output, convert_from_types, damage_types)

    for item in output:
        message_type = item["message_type"]
        message = item["message"]
        print(f"\t{message_type}")
        print(message)


if __name__ == "__main__":
    main()
