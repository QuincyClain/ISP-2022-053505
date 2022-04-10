import inspect
import re



class Yaml_parser:
    count = 0

    @staticmethod
    def dumps(obj):
        yaml_line = ''
        if inspect.isroutine(obj):
            atributes = inspect.getmembers(obj)
            yaml_line += '\n'
            for elem in atributes:
                if elem[0] == 'name':
                    yaml_line += Yaml_parser.dumps(elem[0]) + ': ' + Yaml_parser.dumps(elem[1])
                    yaml_line += '\n'
                elif elem[0] == 'code':
                    yaml_line += Yaml_parser.dumps(elem[0]) + ': ' + Yaml_parser.dumps(str(elem[1])) + '\n'
                elif elem[0] == 'globals':
                    yaml_line += Yaml_parser.dumps(elem[0]) + ': ['
                    for elem in atributes:
                        if elem[0] == 'code':
                            for name in elem[1].co_names:
                                if name in obj.globals:
                                    yaml_line += Yaml_parser.dumps(name)
                                    yaml_line += ','
                    yaml_line = yaml_line[:-1]
                    yaml_line += ']\n'
            yaml_line = yaml_line[:-1]
            yaml_line += '\n'
        elif isinstance(obj, (list, tuple)):
            for elem in obj:
                yaml_line += '- '
                yaml_line += Yaml_parser.dumps(elem) + '\n'
            yaml_line = yaml_line[:-1]
        elif isinstance(obj, dict):
            sorted_tuple = sorted(obj.items(), key=lambda x: x[0])
            obj = dict(sorted_tuple)
            for i in obj.items():
                yaml_line += "\n" + (Yaml_parser.count * "  ") + Yaml_parser.dumps(i[0])
                if isinstance(i[1], (str, int)):
                    yaml_line += ": " + Yaml_parser.dumps(i[1])
                elif isinstance(i[1], dict):
                    Yaml_parser.count += 1
                    yaml_line += ":"
                    for j in i[1].items():
                        yaml_line += "\n" + Yaml_parser.count * "  " + Yaml_parser.dumps(j[0]) + ": "
                        if isinstance(j[1], dict):
                            Yaml_parser.count += 1
                        yaml_line += Yaml_parser.dumps(j[1])
                elif isinstance(i[1], (list, tuple)):
                    yaml_line += ":\n" + Yaml_parser.dumps(i[1])
            Yaml_parser.count = 0
        elif isinstance(obj, bool):
            if obj:
                yaml_line += 'true'
            else:
                yaml_line += 'false'
        elif isinstance(obj, (int, float)):
            yaml_line += str(obj)
        elif isinstance(obj, str):
            obj = obj.replace('\"', '\\\"')
            yaml_line += obj
        elif obj is None:
            yaml_line += "null"
        else:
            raise ValueError(obj)
        return yaml_line


    def dump(obj, file):
        with open(file, 'w') as f:
            f.write(Yaml_parser.dumps(obj))
            f.close()
    

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
                        key = Yaml_parser.loads(colonstr[0])
                        if colonstr[1] == "{":
                            dictflag = 1
                            obj[key] = {}
                        else:
                            obj[key] = Yaml_parser.loads(colonstr[1])
                    else:
                        tempkey = Yaml_parser.loads(colonstr[0])
                        obj[key][tempkey] = Yaml_parser.loads(colonstr[1])
                else:
                    if str.find("}"):
                        dictflag = 0
        elif str.startswith("["):
            temp = str.replace("[", '').replace("]", '').split(" ")
            temp1 = []
            for i in temp:
                temp1.append(Yaml_parser.loads(i))
            return temp1
        elif str.endswith(","):
            temp = str.replace(",", '')
            return Yaml_parser.loads(temp)
        elif str.endswith("\""):
            temp = str.replace("\"", '')
            return Yaml_parser.loads(temp)
        elif str.isdigit():
            return int(str)
        elif re.search(name, str).start() == 0:
            if str == "true":
                return True
            elif str == "false":
                return False
            return str
        return obj
