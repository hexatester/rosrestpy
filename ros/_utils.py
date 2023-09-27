from cattrs import Converter
from typing import Any, Dict, Union


def clean_key(d: Dict[str, Any]) -> dict:
    """Replace - with _ and remove . from key

    Args:
        d (Dict[str, Any]): Raw dict data from ros

    Returns:
        dict: Cleaned data ready to be used as python object props value
    """
    nd = dict()
    for k, v in d.items():
        k = k.replace("-", "_")
        k = k.replace(".", "")
        nd[k] = v
    return nd


def clean_data(d: Dict[str, Any]) -> dict:
    """Clean raw data from ros recursively

    Args:
        d (Dict[str, Any]): Data from ros

    Returns:
        dict: Cleaned data
    """
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


def clean_filters(d: Dict[str, Any]) -> Dict[str, Any]:
    """Replace _ with - on every key on data for query in url

    Args:
        d (Dict[str, Any]): Data to be clean

    Returns:
        Dict[str, Any]: Cleaned data
    """
    if not d:
        return d
    translation_table = str.maketrans("_", "-")
    return {k.translate(translation_table): v for k, v in d.items()}


def clean_before_put(d: Dict[str, Any]) -> dict:
    """Replace _ with - on every key on data for PUT request

    Args:
        d (Dict[str, Any]): Data to be clean

    Returns:
        dict: cleaned data
    """
    if not d:
        return d
    nd = {k.replace("_", "-"): v for k, v in d.items() if v is not None}
    nd.pop("id", None)
    return nd


def _union_str_int(v: str, t: Any) -> Union[str, int]:
    if v.isdigit():
        return int(v)
    return v


def make_converter() -> Converter:
    """Making converter for cattrs

    Returns:
        Converter: cattrs converter
    """
    c = Converter()
    # Main
    c.register_structure_hook(Union[int, str], _union_str_int)
    return c
