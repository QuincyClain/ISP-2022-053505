import os
import re
import yaml



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
    

    def loads(str):
        name = r'[a-zA-z0-9_]'
        obj = dict()
        key = ""
        nstr = str.split("\n")
        dictflag = 0
        if str.startswith(""):
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
