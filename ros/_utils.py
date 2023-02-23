from attrs import asdict
from cattrs import Converter
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, Union, TypeVar

if TYPE_CHECKING:
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
        if v != None:
            nd[k] = v
    return nd


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
    def setters(self: "BM", values: List[T]):
        idattr = "id"
        existed = self.simple
        updated: List[Tuple[T, ...]] = list()
        news: List[T] = list()
        results: List[T] = list()
        for queue in values:
            exist = filter(lambda x: getattr(x, idattr) == getattr(queue, id), existed)
            if exist:
                e: T = set(exist)[0]
                assert e
                if e != queue:
                    updated.append((e, queue))
            else:
                news.append(queue)
        for update in updated:
            old, new = update
            _id = getattr(old, idattr)
            data = asdict(new, True)
            newdata = dict_diff(asdict(old), asdict(new))
            res = self.ros.patch_as(self.url + f"{url}/{_id}", cls, newdata)
            if res:
                results.append(res)
        for new in news:
            data = asdict(new)
            data.pop(idattr)
            res = self.ros.put_as(self.url + f"{url}", cls, data)
            if res:
                results.append(res)
        return results

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
