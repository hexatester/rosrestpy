# RosRestPy

[![PyPi Package Version](https://img.shields.io/pypi/v/rosrestpy)](https://pypi.org/project/rosrestpy/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/rosrestpy)](https://pypi.org/project/rosrestpy/)
[![LICENSE](https://img.shields.io/github/license/hexatester/rosrestpy)](https://github.com/hexatester/rosrestpy/blob/main/LICENSE)

RouterOS v7 REST API python module

## RouterOS v7 REST API Support

Not all types and methods of the RouterOS v7 REST API are supported, yet.
Finding any bugs? Please [Create Issue](https://github.com/hexatester/rosrestpy/issues)

## Installing

You can install or upgrade rosrestpy with:

```bash
pip install rosrestpy --upgrade
```

## Example

```python
from ros import Ros

# Initiate Ros object
ros = Ros("https://192.168.88.1/", "admin", "")


# Check cpu load
if ros.system.resource.cpu_load > 90:
    print(f"{ros.system.identity}'s CPU > 90%")

# Print all interface name
for interface in ros.interface():
    print(interface.name)

# Finding specific queue
queues = ros.queue.simple(name="Hotspot")
if len(queues) == 1:
    queue = queues[0]
    print(f"Usage {queue.bytes}")

# Adding new /simple/queue
from ros.queue import SimpleQueue
new_queue = SimpleQueue(name="Test", target="192.168.88.0/24", max_limit="10M/10M", disabled=True)
new_queue = ros.queue.simple.add(new_queue)
print(new_queue)

# Using /tool/bandwith-test
bw_tests = ros.tool.bandwith_test("172.16.0.1", "3s", "admin", direction="both")
result_bw_test = bw_tests[-1]
print(f"Download {result_bw_test.rx_total_average}")
print(f"Upload {result_bw_test.tx_total_average}")
```

## Resources

The [RouterOS REST API](https://help.mikrotik.com/docs/display/ROS/REST+API) is the technical reference for `rosrestpy`.

## Contributing

Contributions of all sizes are welcome. Please review our [contribution guidelines](https://github.com/hexatester/rosrestpy/blob/main/CONTRIBUTING.md "How To Contribute") to get started. You can also help by [reporting bugs or feature requests](https://github.com/hexatester/rosrestpy/issues/new/choose).

## Open Source Notice

Big thanks to [attrs](https://www.attrs.org/) and [cattrs](https://catt.rs/) as the bases of rosrestpy, without them this module creation would be very tedious!
