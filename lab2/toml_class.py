import abstract_parser
import toml_parser
import serialize_to_dict


class TOML(abstract_parser.AbstractParser):
    def dump(self, obj, file):
        serialized_obj = serialize_to_dict.serialize(obj)
        return toml_parser.Toml_parser.dump(serialized_obj, file)


    def dumps(self, obj):
        serialized_obj = serialize_to_dict.serialize(obj)
        return toml_parser.Toml_parser.dumps(serialized_obj)


    def loads(self, obj):
        return toml_parser.Toml_parser.loads(obj)


    def load(self, file):
        return toml_parser.Toml_parser.load(file)