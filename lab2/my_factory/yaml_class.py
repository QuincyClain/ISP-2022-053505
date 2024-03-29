from parsers import abstract_parser
from parsers import yaml_parser
from intermediate_parser import serialize_to_dict


class YAML(abstract_parser.AbstractParser):
    def dump(self, obj, file):
        return yaml_parser.Yaml_parser.dump(obj, file)


    def dumps(self, obj):
        serialized_obj = serialize_to_dict.serialize(obj)
        return yaml_parser.Yaml_parser.dumps(serialized_obj)


    def loads(self, obj):
        return yaml_parser.Yaml_parser.loads(obj)


    def load(self, file):
        return yaml_parser.Yaml_parser.load(file)