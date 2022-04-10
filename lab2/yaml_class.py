import abstract_parser
import yaml_parser


class YAML(abstract_parser.AbstractParser):
    def dump(self, obj, file):
        return yaml_parser.Yaml_parser.dump(obj, file)


    def dumps(self, obj):
        return yaml_parser.Yaml_parser.dumps(obj)


    def loads(self, obj):
        return yaml_parser.Yaml_Parser.loads(obj)


    def load(self, file):
        return yaml_parser.Yaml_Parser.load(file)