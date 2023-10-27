# How To Contribute

Every open source project lives from the generous help by contributors that sacrifice their time and rosrestpy is no different. To make participation as pleasant as possible, this project adheres to the [Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct.html) by contributor-covenant.

## Setting things up

### Setup

1. Fork the rosrestpy repository to your GitHub account.

2. Clone your forked repository of rosrestpy to your computer:

    ```bash
    git clone https://github.com/<your username>/rosrestpy
    cd rosrestpy
    ```

3. Add a track to the original repository:

    ```bash
    git remote add upstream https://github.com/hexatester/rosrestpy
    ```

4. Install dependencies with [python-poetry](https://python-poetry.org/):

    ```bash
    pip install poetry
    poetry install --no-root
    ```

### IDE

Recommended linter (linting) `mypy` and code formater `black`.

## Finding something to do

If you already know what you'd like to work on, you can skip this section.

If you have an idea for something to do, first check if it's already been filed on the [issue tracker](https://github.com/hexatester/rosrestpy/issues). If so, add a comment to the issue saying you'd like to work on it, and we'll help you get started! Otherwise, please file a new issue and assign yourself to it.

Another great way to start contributing is by writing tests. Tests are really important because they help prevent developers from accidentally breaking existing code, allowing them to build cool things faster.

That being said, we want to mention that we are very hesitant about adding new requirements to our projects. If you intend to do this, please state this in an issue and get a verification from the maintainer.

## Implementing function

This including property.

## Implementing types

All types must be convertable from and to the REST API with the help of [attrs modoule](https://pypi.org/project/attrs/ "Classes Without Boilerplate") for implementing object protocols and [cattrs module](https://pypi.org/project/cattrs/ "Composable complex class support for attrs and dataclasses.") for structuring and unstructuring data.

Using `attr.dataclass` as decorator for class. If the type is immutable, please [enable slots](https://github.com/hexatester/rosrestpy/blob/main/ros/system/health.py#L3 "example enabling slots") for performance improvement.

Notes on converting data from REST API to python type

- `.id` property will be changed to `id`
- All property with `-` will be replaced with `_`

Notes on converting data from python type to REST API

- `id` property will ble changed to `.id`
- All property with `-` will be replaced with `_`

## Base classes usage

Base (`ros._base`) usage

### Baseprop

This class have implementtation for .print and .set methods for implementing specific command that only return single object, such as `/ip/cloud`.

```python
from ros._base import BaseProp

class Cloud:
    ddns_enabled: bool
    # ...

ip_cloud = BaseProp(ros, "/ip/cloud", Cloud)
ip_cloud.print()
```

### Baseprops

This class have implementtation for .add, .delete, .disable, .enable, .print, .remove, .set, and .unset methods for implementing specific command that return multiple objects, such as `/queue/simple`.

```python
from ros._base import BaseProps

class QueueSimple:
    name: str
    # ...

ip_cloud = BaseProps(ros, "/queue/simple", QueueSimple)
ip_cloud.print()
```

## Adding doctypes or documentation

Not yet a priority, but we welcome pull request.
