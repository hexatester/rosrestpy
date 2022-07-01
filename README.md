# RosRestPy

[![PyPi Package Version](https://img.shields.io/pypi/v/rosrestpy)](https://pypi.org/project/rosrestpy/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/rosrestpy)](https://pypi.org/project/rosrestpy/)
[![LICENSE](https://img.shields.io/github/license/hexatester/rosrestpy)](https://github.com/hexatester/rosrestpy/blob/main/LICENSE)

RouterOS v7 REST API python module

## RouterOS v7 REST API Support

Not all types and methods of the RouterOS v7 REST API are supported, yet.

## Installing

You can install or upgrade rosrestpy with:

```bash
pip install rosrestpy --upgrade
```

## Example

```python
from ros import Ros

ros = Ros("https://192.168.88.1/", "admin", "")
if ros.system.resource.cpu_load > 90:
    print(f"{ros.system.identity}'s CPU > 90%")
```

## Resources

The [RouterOS REST API](https://help.mikrotik.com/docs/display/ROS/REST+API) is the technical reference for `rosrestpy`.

## Contributing

Contributions of all sizes are welcome. Please review our [contribution guidelines](https://github.com/hexatester/rosrestpy/blob/main/CONTRIBUTING.md "How To Contribute") to get started. You can also help by [reporting bugs or feature requests](https://github.com/hexatester/rosrestpy/issues/new/choose).
