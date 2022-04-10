import abstract_parser
import json_parser


class JSON(abstract_parser.AbstractParser):
    def dump(self, obj, file):
        return json_parser.Json_Parser.dump(obj, file)

    
    def dumps(self, obj):
        return json_parser.Json_Parser.dumps(obj)

    
    def loads(self, obj):
        return json_parser.Json_Parser.loads(obj)
        

    def load(self, file):
        return json_parser.Json_Parser.load(file)