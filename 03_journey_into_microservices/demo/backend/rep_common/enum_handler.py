from enum import Enum
import json
import os


class SharedEnum(Enum):
    def __new__(self, value):
        enum_name = self.__name__
        obj = object.__new__(self)
        obj._value_ = get_enum_value_from_json(enum_name, value)
        return obj

    @classmethod
    def to_dict(cls):
        return {name: obj.value for name, obj in cls.__members__.items()}

micro_service_enums = {}
def get_enum_value_from_json(enum_name:str, enum_member_name:str, source_name: str = None):
    microservice_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    microservice_key_name = source_name or microservice_root_dir

    # Checks whether the microservice enums object exists in 'micro_service_enums'
    if microservice_key_name in micro_service_enums:
        enums_values = micro_service_enums.get(microservice_key_name)
    else:
        # Builds the path to the enums json file according to the source_name
        if source_name == 'rep_common':
            json_path = os.path.join(microservice_root_dir, 'rep_common', 'enums', 'enums_json.json')
        else:
            json_path = os.path.join(microservice_root_dir, 'enums', 'enums_json.json')
        with open(json_path) as enums_json:
            enums_values = json.load(enums_json)

    micro_service_enums[microservice_key_name] = enums_values
    # If enum_name exists in the enums_values object, return the relevant value
    # Otherwise, checks in rep_common
    # If the enum_name was not found in rep_common, raises an error
    if enum_name in enums_values:
        return enums_values.get(enum_name).get(enum_member_name)
    elif source_name is None:
        return get_enum_value_from_json(enum_name,enum_member_name, 'rep_common')
    else:
        raise ValueError(f"{enum_name} was not found in the JSON file")
