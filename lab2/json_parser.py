import ast
import serialize_to_dict


class Json_Parser:
    @staticmethod
    def dumps(obj):
        json_line = ''
        if isinstance(obj, dict):
            for key, val in obj.items():
                if key == 'tuple' or key == 'list':
                    json_line += '['
                    if len(val) == 0:
                        json_line+= '  '
                    for item in val:
                        json_line += Json_Parser.dumps(item)
                        json_line += ', '
                    json_line = json_line[:-2]
                    json_line += ']'
                elif key == 'dict':
                    json_line += '{'
                    if len(val) == 0:
                        json_line += '  '
                    for item_key, item_val in val.items():
                        json_line += Json_Parser.dumps(item_key) + ': ' + Json_Parser.dumps(item_val)
                        json_line += ', '
                    json_line = json_line[:-2]
                    json_line += '}'
                json_line += ', '
            json_line = json_line[:-2]
        #LOL
        elif isinstance(obj, bool):
            if obj:
                json_line += 'true'
            else:
                json_line += 'false'
        elif isinstance(obj, (int, float)):
            json_line += str(obj)
        elif isinstance(obj, str):
            json_line += '\"' + obj + '\"'
        return json_line
    

    @staticmethod
    def dump(obj, file):
        with open(file, 'w') as f:
            f.write(Json_Parser.dumps(obj))
            f.close()


    @staticmethod
    def loads(obj):
        diff_str = obj.replace("true", "True").replace("false", "False")
        my_dict = {}
        my_dict = ast.literal_eval(diff_str)
        return serialize_to_dict.deserialize(my_dict)
    

    @staticmethod
    def load(file):
        with open(file, 'r') as f:
            json_string = f.read()
            my_dict = Json_Parser.loads(json_string)
            f.close()
        return my_dict
        
