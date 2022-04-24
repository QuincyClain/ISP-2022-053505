import qtoml

from my_factory import a_factory
from intermediate_parser import serialize_to_dict
import math
import os



#globals
a = 10
b = 20
c = 42


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.married = True
        self.autistic = False
        self.my_dict = {"a": 1, "b": {"lol": 2}}
        self.my_list = [1, 2, 3]
        self.my_tuple = (1, 2, 3)

    def introduce(self):
        str_age = str(self.age)
        print("Hello my name is " + self.name + " and I'm " + str_age + " years old.")


#func for serialize-check
def fa(x):
    return math.sin(x * a * c)


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def main():
    obj = Person("Vlad", 19)
    obj_dict = obj.__dict__

    #create concrete parser
    parser = a_factory.Factory()
    json_parser = parser.create_parser('JSON')
    yaml_parser = parser.create_parser('YAML')
    toml_parser = parser.create_parser('TOML')

    yaml_ser_func = yaml_parser.dumps(fa)
    yaml_des_func = yaml_parser.loads(yaml_ser_func)
    print(yaml_des_func(10))

    toml_ser_func = toml_parser.dumps(fa)
    toml_des_func = toml_parser.loads(toml_ser_func)

    print(toml_ser_func)
    print(toml_des_func(10))
    func_to_dict = serialize_to_dict.serialize(fa)
    ser = qtoml.dumps(func_to_dict)
    to_dict = qtoml.loads(ser)
    print(to_dict)
    dict_to_func = serialize_to_dict.deserialize(to_dict)
    print(dict_to_func(10))


if __name__ == "__main__":
    main()
