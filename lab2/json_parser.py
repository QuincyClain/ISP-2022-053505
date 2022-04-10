import inspect
import re


class Json_Parser:

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


    @staticmethod
    def dump(obj, file):
        with open(file, 'w') as f:
            f.write(Json_Parser.dumps(obj))
            f.close()


    @staticmethod
    def loads(str):
        name = r'[a-zA-z0-9_]'
        obj = dict()
        key = ""
        nstr = str.split("\n")
        dictflag = 0
        if str.startswith("{"):
            for i in nstr:
                if i.find(": ") != -1:
                    colonstr = i.split(": ")
                    if dictflag == 0:
                        key = Json_Parser.loads(colonstr[0])
                        if colonstr[1] == "{":
                            dictflag = 1
                            obj[key] = {}
                        else:
                            obj[key] = Json_Parser.loads(colonstr[1])
                    else:
                        tempkey = Json_Parser.loads(colonstr[0])
                        obj[key][tempkey] = Json_Parser.loads(colonstr[1])
                else:
                    if str.find("}"):
                        dictflag = 0
        elif str.startswith("["):
            temp = str.replace("[", '').replace("]", '').split(" ")
            temp1 = []
            for i in temp:
                temp1.append(Json_Parser.loads(i))
            return temp1
        elif str.endswith(","):
            temp = str.replace(",", '')
            return Json_Parser.loads(temp)
        elif str.endswith("\""):
            temp = str.replace("\"", '')
            return Json_Parser.loads(temp)
        elif str.isdigit():
            return int(str)
        elif re.search(name, str).start() == 0:
            if str == "true":
                return True
            elif str == "false":
                return False
            return str
        return obj


    def load(file):
        with open(file, 'r') as f:
            json_string = f.read()
            my_dict = Json_Parser.loads(json_string)
            f.close()
        return my_dict
