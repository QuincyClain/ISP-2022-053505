import inspect

class Json_Parser:
    @staticmethod
    def dump(obj, file):
        with open(file, 'w') as f:
            f.write(Json_Parser.dumps(obj))
            f.close()

    @staticmethod
    def dumps(obj):
            json_line = ''
            if inspect.isroutine(obj):
                atributes = inspect.getmembers(obj)
                json_line += '{\n'
                for elem in atributes:
                    if elem[0] == '__name__':
                        json_line += Json_Parser.dumps(elem[0]) + ': ' + Json_Parser.dumps(elem[1])
                        json_line += ',\n'
                    elif elem[0] == '__code__':
                        json_line +=Json_Parser.dumps(elem[0]) + ': ' + Json_Parser.dumps(str(elem[1])) + ',\n'
                    elif elem[0] == '__globals__':
                        json_line +=Json_Parser.dumps(elem[0]) +': ['
                        for elem in atributes:
                            if elem[0] == '__code__':
                                for name in elem[1].co_names:
                                    if name in obj.__globals__:
                                        json_line += Json_Parser.dumps(name)
                                        json_line += ','
                        json_line = json_line[:-2]
                        json_line += '],\n'
                json_line = json_line[:-2]
                json_line += '\n}'
            elif isinstance(obj, (list, tuple)):
                json_line += '['
                for elem in obj:
                    json_line += Json_Parser.dumps(elem)
                    json_line += ', '
                json_line = json_line[:-2]
                json_line += ']'
            elif isinstance(obj, dict):
                json_line += '{\n'
                for key, val in obj.items():
                    json_line += Json_Parser.dumps(key) + ': ' + Json_Parser.dumps(val) + ',\n'
                json_line = json_line[:-2]
                json_line += '\n}'
            elif isinstance(obj, bool):
                if obj:
                    json_line += 'true'
                else:
                    json_line += 'false'
            elif isinstance(obj, (int, float)):
                json_line += str(obj)
            elif isinstance(obj, str):
                obj = obj.replace('\"', '\\\"')
                json_line += '\"' + obj + '\"'
            elif obj is None:
                json_line += "null"
            else:
                raise ValueError(obj)
            return json_line
