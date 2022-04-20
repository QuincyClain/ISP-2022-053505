import abstract_parser
import json_parser
import serialize_to_dict


class JSON(abstract_parser.AbstractParser):
    def dump(self, obj, file):
        serialized_obj = serialize_to_dict.serialize(obj)
        return json_parser.Json_Parser.dump(serialized_obj, file)

    
    def dumps(self, obj):
        serialized_obj = serialize_to_dict.serialize(obj)
        return json_parser.Json_Parser.dumps(serialized_obj)

    
    def loads(self, obj):
        return json_parser.Json_Parser.loads(obj)
        

    def load(self, file):
        return json_parser.Json_Parser.load(file)