from typing import Union


def group_by_age(people: list[dict[str, Union[int, str]]]) -> dict[int, list[str]]:
    group = {}
    for person in people:
        group.setdefault(person['age'], []).append(person['name'])


    return group


people = [
    {
        "name": "ali",
        "age": 13
    },
     {
        "name": "vali",
        "age": 15
    },
     {
        "name": "sami",
        "age": 10
    },
     {
        "name": "jon",
        "age": 15
    },
]

result = group_by_age(people)
print(result)