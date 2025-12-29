from typing import Any


def NULL_not_found(object: Any) -> int:

    if object is None:
        print(f"Nothing: {object} <class 'NoneType'>")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} <class 'Float'>")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} <class 'bool'>")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} <class 'int'>")
    elif isinstance(object, str) and object == '':
        print(f"Empty: {object} <class 'str'>")
    else:
        print("Type not found")
        return 1
    return 0
