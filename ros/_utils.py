from cattrs import Converter
from typing import Any, Dict, List, Type, Union, TypeVar

from ._base import BM


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


def _union_str_int(v: str, t: Any) -> Union[str, int]:
    if v.isdigit():
        return int(v)
    return v


def dict_diff(old: Dict[str, Any], new: Dict[str, Any]) -> Dict[str, Any]:
    results: Dict[str, Any] = dict()
    for o, ov in old.items():
        nv = new.get(o)
        if nv is None:
            continue
        if nv == ov:
            results[o] = nv
    return results


T = TypeVar("T", bound=object)


def make_setters(url: str, cls: Type[T]):
    def setters(self: BM, values: List[T]):
        pass

    return setters


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
