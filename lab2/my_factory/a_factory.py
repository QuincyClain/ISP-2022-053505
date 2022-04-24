from my_factory import json_class
from my_factory import yaml_class
from my_factory import toml_class


class Factory:
    def create_parser(self, format):
        parser = None
        if format == "JSON":
            parser = json_class.JSON()
            return parser
        elif format == "YAML":
            parser = yaml_class.YAML()
            return parser
        elif format == "TOML":
            parser = toml_class.TOML()
            return parser
        else:
            raise ValueError(format)

#factory

