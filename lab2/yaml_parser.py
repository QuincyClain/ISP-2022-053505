import os
import yaml
from yaml import Loader

import serialize_to_dict


class Yaml_parser:

    @staticmethod
    def dumps(obj):
        file = 'temp.yml'
        Yaml_parser.dump(obj, file)
        with open(file, 'r') as f:
            yaml_line = f.read()
        os.remove(file)
        return yaml_line

    @staticmethod
    def dump(obj, file):
        with open(file, 'w') as f:
            f.write(yaml.safe_dump(obj))
            f.close()
        return file

    @staticmethod
    def load(my_file):
        stream = open(my_file, 'r')
        obj = yaml.load(stream, Loader=Loader)
        return serialize_to_dict.deserialize(obj)

    @staticmethod
    def loads(my_str):
        file = 'load_temp.yml'
        with open(file, 'w') as f:
            f.write(my_str)
            f.close()
        obj = Yaml_parser.load(file)
        os.remove(file)
        return obj

