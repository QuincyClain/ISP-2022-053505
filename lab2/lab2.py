import json
import yaml
import factory
from json_parser import Json_Parser
import serialize_to_dict
import math

import types


#globals
a = 10
b = 20
c = 42

#class for serialize-check
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
    a = 123
    return math.sin(x * a * c)


def fact(n):
    print(a)
    print(b)
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

#func for serialize-check
def Sum_number():
    print(a)
    print(b)
    return a+b


def main():


    #json to dict check
    x = '{ "name":"Vlad", "age":19, "city":"Minsk"}'
    y = json.loads(x)
    print(y["name"], y["age"], y["city"])

    #just an object from to test
    obj = Person("Vlad", 19)
    obj_dict = obj.__dict__

    #create concrete parser
    parser = factory.Factory()
    json_parser = parser.create_parser('JSON')
    yaml_parser = parser.create_parser('YAML')

    json_ser_func = json_parser.dumps(fa)
    print(json_ser_func)

    ser_obj = json_parser.dumps(obj_dict)
    print(ser_obj)
    print("aaaaa")


    #json_des_func = json_parser.loads(json_ser_func)
    #print(json_des_func(5))
    yaml_ser_func = yaml_parser.dumps(fa)
    yaml_des_func = yaml_parser.loads(yaml_ser_func)
    print(yaml_des_func(10))





if __name__ == "__main__":
    main()
