from typing import Any, Dict


def clean_key(d: Dict[str, Any]) -> dict:
    nd = dict()
    for k, v in d.items():
        k = k.replace("-", "_")
        if k == ".id":
            k = "id"
        nd[k] = v
    return nd
