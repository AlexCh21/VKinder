
from typing import List

	"""
	модуль параметров поиска описывает свойства искомого пользователя
	"""

class BaseField:
    mytype = str

    def __init__(self, name, value, weight=1):
        self.check_type_name(name)
        self.check_type_value(value)
        self.check_type_weight(weight)

        self.name = name
        self.value = value
        self.weight = weight

    @staticmethod
    def check_type_name(name):
        if isinstance(name, str):
            return name
        raise TypeError('имя должно быть экземпляром string')

    @staticmethod
    def check_type_weight(weight):
        if isinstance(weight, int):
            return weight
        raise TypeError('Вес должен быть целым числом')

    def check_type_value(self, value):
        if isinstance(value, self.mytype):
            return value
        raise TypeError('значение должно быть экземпляром %s' % type(self.mytype))


class StringField(BaseField):
    mytype = str


class ListField(BaseField):
    mytype = list


class SearchParams:
    def __init__(self, fields: List[BaseField]) -> None:
        self.registry = dict()
        for field in fields:
            self.registry[field.name] = field
