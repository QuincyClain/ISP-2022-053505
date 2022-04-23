import toml
import serialize_to_dict


class Toml_parser:

    def dumps(obj):
        return toml.dumps(obj)

    def loads(my_str):
        toml_obj = toml.loads(my_str)
        my_obj = serialize_to_dict.deserialize(toml_obj)
        return my_obj



