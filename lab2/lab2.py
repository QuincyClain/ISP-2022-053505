import json
import yaml
import factory
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
        self.dict = {"a": 1, "b": {"lol": 2}}
        self.my_list = [1, 2, 3]

    
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
    x =  '{ "name":"Vlad", "age":19, "city":"Minsk"}'
    y = json.loads(x)
    print(y["name"], y["age"], y["city"])

    #just an object from to test
    obj = Person("Vlad", 19)
    obj_dict = obj.__dict__
        
    print(serialize_to_dict.serialize(obj_dict))
    print(serialize_to_dict.serialize(fa))

    ser_func = serialize_to_dict.serialize(fa)
    des_func = serialize_to_dict.deserialize(ser_func)

    print(des_func(5))

    #create concrete parser
    parser = factory.Factory()
    json_parser = parser.create_parser('JSON')
    yaml_parser = parser.create_parser('YAML')


    #json_string = json.dumps(obj_dict)
    tupple = ("Vlad", "Alex")
    json_parser_string = json_parser.dumps(obj_dict)
    json_parser_func = json_parser.dumps(fact)
    json_parser.dump(fact, 'serialize_json_func.txt')
    json_parser.dump(obj_dict, 'serialize_json_obj.txt')

    #yaml_strin = yaml.dumps(obj_dict)
    with open('yaml_serialize.yml', 'w') as f:
        f.write(yaml.safe_dump(obj_dict))
        f.close()
    yaml_parser_string = yaml_parser.dumps(tupple)
    #yaml_parser_func = yaml_parser.dumps(fact)
    yaml_parser.dump(obj_dict, 'my_yaml_serialize.yml')

    print("JSON: ")
    #print(json_string)
    print(json_parser_string)
    print(json_parser_func)

    print("YAML: ")
    print(yaml_parser_string)
   # print(yaml_parser_func)
    #loads_object
    #deserealize_object = json_parser.loads(json_parser_string)
   # print(deserealize_object)

    #checking bool after loads
    #if(deserealize_object["married"]):
      #  print('it is TRUE!')

   # deserealize_object = Person(deserealize_object["name"], deserealize_object["age"])
  #  print(type(deserealize_object))

    #json_loads_list

    list_str = json_parser.dumps([1,2,3])
    print(list_str)
    #my_list = json_parser.loads(list_str)
   # print(my_list)
    #my_list.pop()
   # print(my_list)

    #json_laods_tuple
    my_tuple = ("vlad", "alex", "angel")
    my_list = ["vlad", "alex", "angel"]
    print(my_tuple)
    print(my_list)
    lol = json_parser.dumps(my_tuple)
   # my_des_tuple = json_parser.loads(lol)
    #print(my_des_tuple)
   # print(type(my_des_tuple))

    '''
    #json_load
    my_file_dict = json_parser.load('serialize_json_obj.txt')
    print(my_file_dict)
    print(type(my_file_dict))
    '''


if __name__ == "__main__":
    main()
