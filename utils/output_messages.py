return_char = "\\n"
any_char = f"(.|{return_char})*"
level = f"{any_char}l: (9)(\\d)"


def retaliation_messages(skills: str, damage_types: str):
    output = [{
        "message_type": "skills and damage",
        "message": f"/retaliation{any_char}({skills}){level}/",
    }, {
        "message_type": "damage",
        "message": f"/retaliation{any_char}({damage_types}){level}/",
    }, {
        "message_type": "skills",
        "message": f"/retaliation{any_char}({skills}){level}/",
    }, {
        "message_type": "any retaliation",
        "message": f"/retaliation{level}/"
    }]
    return output


def player_messages(skills: str, damage_types: str):
    output = [{
        "message_type": "skill and damage",
        "message": f"/({damage_types}) damage{return_char}{any_char}({skills}){return_char}{level}/",
    }, {
        "message_type": "damage",
        "message": f"/({damage_types}) damage{level}/",
    }]
    return output


def pet_messages(skills: str, damage_types: str):
    insert = "bonus to all pets"
    output = [{
        "message_type": "skill and damage",
        "message": f"/({skills}){return_char}{any_char}{insert}{any_char}({damage_types}) damage{return_char}{level}/",
    }, {
        "message_type": "skills",
        "message": f"/({skills}){return_char}{any_char}{insert}{level}/",
    }, {
        "message_type": "damage",
        "message": f"/{insert}{any_char}({damage_types}) damage{return_char}{level}/",
    }, {
        "message_type": "any pets",
        "message": f"/{insert}{level}/"
    }]
    return output


def add_both_skills_message(output: list, classes_list: list):
    output.append(
        {
            "message_type": "get +skills to both classes",
            "message": f"/((all skills{return_char})|({classes_list[0]}{any_char}{classes_list[1]})|({classes_list[1]}{any_char}{classes_list[0]})){level}/",
        }
    )


def add_convert_types_message(output: list, convert_from_types, damage_types):
    if len(convert_from_types) > 0:
        output.append(
            {
                "message_type": "convert",
                "message": f"/({convert_from_types}) damage converted to ({damage_types}) damage{return_char}{level}/",
            }
        )
        output.append(
            {
                "message_type": "convert no level",
                "message": f"/({convert_from_types}) damage converted to ({damage_types}) damage{return_char}/",
            }
        )
