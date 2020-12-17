from utils.character_management import add_skills_from_classes, extend_skills
from utils.damage_type_parsers import (
    check_damage_source,
    calculate_damage_types,
    add_elemental,
)


return_char = "\\n"
any_char = f"(.|{return_char})*"
level = f"{any_char}l: (9)(\d)"


def main():
    damage_types_list = ["cold"]
    convert_from_types_list = []
    classes_list = [
        "nightblade",
        "arcanist"
    ]
    skills_list = [
        "merciless repertoire",
        "star pact",
        "blade spirit",
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

    output = []

    if damage_source == "retaliation":
        output.append(
            {
                "message_type": "skills and damage",
                "message": f"/retaliation{any_char}({skills}){level}/",
            }
        )
        output.append(
            {
                "message_type": "damage",
                "message": f"/retaliation{any_char}({damage_types}){level}/",
            }
        )
        output.append(
            {
                "message_type": "skills",
                "message": f"/retaliation{any_char}({skills}){level}/",
            }
        )
        output.append(
            {
                "message_type": "any retaliation",
                "message": f"/retaliation{level}/"
            }
        )
    elif damage_source == "player":
        output.append(
            {
                "message_type": "skill and damage",
                "message": f"/({damage_types}) damage{return_char}{any_char}({skills}){return_char}{level}/",
            }
        )
        output.append(
            {
                "message_type": "damage",
                "message": f"/({damage_types}) damage{level}/",
            }
        )
    elif damage_source == "pet":
        insert = "bonus to all pets"
        output.append(
            {
                "message_type": "skill and damage",
                "message": f"/({skills}){return_char}{any_char}{insert}{any_char}({damage_types}) damage{return_char}{level}/",
            }
        )
        output.append(
            {
                "message_type": "skills",
                "message": f"/({skills}){return_char}{any_char}{insert}{level}/",
            }
        )
        output.append(
            {
                "message_type": "damage",
                "message": f"/{insert}{any_char}({damage_types}) damage{return_char}{level}/",
            }
        )
        output.append(
            {
                "message_type": "any pets",
                "message": f"/{insert}{level}/"
            }
        )

    output.append(
        {
            "message_type": "get +skills to both classes",
            "message": f"/((all skills{return_char})|({classes_list[0]}{any_char}{classes_list[1]})|({classes_list[1]}{any_char}{classes_list[0]})){level}/",
        }
    )
    if len(convert_from_types) > 0:
        output.append(
            {
                "message_type": "convert",
                "message": f"/({convert_from_types}) damage converted to {damage_types} damage{return_char}{level}/",
            }
        )
        output.append(
            {
                "message_type": "convert no level",
                "message": f"/({convert_from_types}) damage converted to {damage_types} damage{return_char}/",
            }
        )

    for item in output:
        message_type = item["message_type"]
        message = item["message"]
        print(f"\t{message_type}")
        print(message)


if __name__ == "__main__":
    main()
