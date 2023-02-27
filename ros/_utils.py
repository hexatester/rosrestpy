from cattrs import Converter
from typing import Any, Dict, Union


def clean_key(d: Dict[str, Any]) -> dict:
    nd = dict()
    for k, v in d.items():
        k = k.replace("-", "_")
        k = k.replace(".", "")
        nd[k] = v
    return nd


def clean_data(d: Dict[str, Any]) -> dict:
    data: Any = None
    if isinstance(d, dict):
        data = clean_key(d)
    elif isinstance(d, list):
        data = list()
        for val in d:
            if isinstance(val, dict):
                data.append(clean_key(val))
            else:
                data.append(val)
    return data


def clean_filters(d: Dict[str, Any]) -> dict:
    if not d:
        return d
    nd = dict()
    for k, v in d.items():
        k = k.replace("_", "-")
        nd[k] = v
    return nd


def clean_before_put(d: Dict[str, Any]) -> dict:
    if not d:
        return d
    d.pop("id")
    nd = dict()
    for k, v in d.items():
        if "_" in k:
            k = k.replace("_", "-")
        if v != None:
            nd[k] = v
    return nd


def _union_str_int(v: str, t: Any) -> Union[str, int]:
    if v.isdigit():
        return int(v)
    return v


def make_converter() -> Converter:
    c = Converter()
    # Main
    c.register_structure_hook(Union[int, str], _union_str_int)
    return c
