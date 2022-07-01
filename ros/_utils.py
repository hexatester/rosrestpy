from cattrs import Converter
from typing import Any, Dict, Union


def clean_key(d: Dict[str, Any]) -> dict:
    nd = dict()
    for k, v in d.items():
        k = k.replace("-", "_")
        if k == ".id":
            k = "id"
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


def setter(self, value):
    # TODO: Implement setter
    pass


def deleter(self, value):
    # TODO: Implement deleter
    pass
