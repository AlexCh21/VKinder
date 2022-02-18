

def eval_lists(one: list, another: list, cost=1) -> int:
    common = []
    for elem in one:
        if elem in another:
            common.append(elem)
    weight = cost * len(common)
    return weight

"""
модуль оценивает общих строковых параметров, таких как:
интересы, город, музыка, книги, фильмы
Возвращает конечный параметр
"""

def eval_city(city, mycity, cost=10):
    match_factor = 10
    if not mycity or not city:
        return 0
    if city == mycity:
        return match_factor * cost
    return 0
