from database.classes import base_classes
from database.skills import base_skills


def add_skills_from_classes(skills, classes):
    for class_name in classes:
        skills.extend(base_classes[class_name])


def extend_skills(skills):
    for skill in list(skills):
        skills.extend(base_skills[skill])
