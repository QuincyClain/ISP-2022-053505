import qtoml
from intermediate_parser import serialize_to_dict


class Toml_parser:

    def dumps(obj):
        return qtoml.dumps(obj)


    def dump(obj, file):
        with open(file, 'w') as f:
            f.write(Toml_parser.dumps(obj))
            f.close()
        return file


    def loads(my_str):
        toml_obj = qtoml.loads(my_str)
        my_obj = serialize_to_dict.deserialize(toml_obj)
        return my_obj

    
    def load(file):
        string_from_file = ''
        with open(file, 'r') as f:
            string_from_file = f.read()
            f.close()
        return Toml_parser.loads(string_from_file)





