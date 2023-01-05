import json
from typing import Mapping, List, Union, Dict, Any
from hashlib import sha256


def _add(res: Dict[str, Any], key: str, k, v):
    n_key = f'{key}.{k}' if key else f'{k}'
    if isinstance(v, List):
        res.update(_inline_list(n_key, v))
    elif isinstance(v, Mapping):
        res.update(_inline_mapping(n_key, v))
    else:
        res[n_key] = f'{v}'


def _inline_list(key: str, d: List) -> Mapping:
    res = {}
    for k, v in enumerate(d):
        _add(res, key, k, v)
    return res


def _inline_mapping(key: str, d: Mapping) -> Mapping:
    res = {}
    for k, v in d.items():
        _add(res, key, k, v)
    return res


def inline(d: Union[Mapping, List]) -> Mapping:
    result = {}
    if not d:
        return result
    if isinstance(d, List):
        result.update(_inline_list('', d))
    elif isinstance(d, Mapping):
        result.update(_inline_mapping('', d))
    return result


class Singer:
    def __init__(self, *, private_key: str, public_key: str):
        self.private_key = private_key,
        self.public_key = public_key

    def get_sign(self, body: Mapping) -> str:
        # все словари и массивы приводим к одномерному виду
        params = inline(body)
        # сортируем
        sorted_keys = list(sorted(params.keys()))
        # конкатенируем значения
        concatenated_values = ''.join([params[k] for k in sorted_keys])
        concatenated_values = f'{self.private_key}{concatenated_values}'
        # вычисляем хеш sha256
        return sha256(concatenated_values.encode()).hexdigest()
