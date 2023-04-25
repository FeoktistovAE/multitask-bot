import pymorphy2 as pymorphy2


morph = pymorphy2.MorphAnalyzer()


def change_declension(city_name: str) -> str:
    split_by_space = city_name.split(' ')
    try:
        changed_declension = ' '.join(
            [morph.parse(i)[0].inflect({'loct'}).word.capitalize() for i in split_by_space]
        )
    except AttributeError:
        return city_name
    if "-" in changed_declension:
        capitalize_after_dash = '-'.join(
            [i.capitalize() for i in changed_declension.split('-')]
        )
        return capitalize_after_dash
    return changed_declension
