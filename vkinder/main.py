
from typing import List
import json
from vkinder.searchparams import SearchParams
from .field_adapters import dummy, city_to_string, split_string
from .evaluators import eval_lists, eval_city


EVALUATORS = {
    'city': eval_city,
    'interests': eval_lists,
    'music': eval_lists,
    'books': eval_lists,
    'movies': eval_lists,
}
ADAPTERS = {
    'city': city_to_string,
    'interests': split_string,
    'music': split_string,
    'books': split_string,
    'movies': split_string,

}


def data_process(search_params: SearchParams, candidates: List[dict]) -> dict:
    """
	Получите подходящих кандидатов, каждый user_raw обрабатывается оценщиками и адаптерами.
	Результат записывается в виде списка идентификаторов.
    """
    assert isinstance(candidates, list)
    data = dict()

    for user_raw in candidates:
        weight = 0
        for field, evaluator in EVALUATORS.items():

            if not user_raw.get(field):
                continue

            if not search_params.registry.get(field):
                continue
            field_obj = search_params.registry[field]

            adapter = ADAPTERS.get(
                field, dummy)

            weight += evaluator(
                adapter(user_raw[field]),
                field_obj.value,
                field_obj.weight,
            )

        data[user_raw['id']] = {'weight': weight, 'user': user_raw}

        filename = 'data_answer.json'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data,
                               sort_keys=False,
                               indent=4,
                               ensure_ascii=False,
                               separators=(',', ': ')))

    return data


def sort_data(data):
    sort_dict = {}
    for uid, user in data.items():
        sort_dict[uid] = user['weight']

    sort_by_weight = dict(sorted(sort_dict.items(), key=lambda item: item[1], reverse=True))

    filename = 'sorted_weight.json'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(sort_by_weight,
                           sort_keys=False,
                           indent=2,
                           ensure_ascii=True,
                           separators=(',', ': ')))

    user_list = []
    for user in sort_by_weight.keys():
        user_list.append(user)
    top_10_list = user_list[0:10]

    print(top_10_list)

    return sort_by_weight


def groups_matching():
    pass
