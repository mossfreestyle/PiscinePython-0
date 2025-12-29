from typing import Any

def all_thing_is_obj(object: Any) -> int:
    obj_type = type(object)

    if isinstance(object, list):
        print(f"List : {obj_type}")
    elif isinstance(object, tuple):
        print(f"Tuple : {obj_type}")
    elif isinstance(object, set):
        print(f"Set : {obj_type}")
    elif isinstance(object, dict):
        print(f"Dict : {obj_type}")
    elif isinstance(object, str):
        print(f"{object} love PSG : {obj_type}")
    else:
        print("type not found")
    return 42