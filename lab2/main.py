from factory import a_factory
import math



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
    #just an object from to test
    obj = Person("Vlad", 19)
    obj_dict = obj.__dict__

    #create concrete parser
    parser = a_factory.Factory()
    json_parser = parser.create_parser('JSON')
    yaml_parser = parser.create_parser('YAML')
    toml_parser = parser.create_parser('TOML')

    json_ser_func = json_parser.dumps(fa)
    json_parser.dump(fa, 'my_json_func.json')
    json_des_func = json_parser.loads(json_ser_func)
    print(json_ser_func)
    print(json_des_func(10))

    ser_obj = json_parser.dumps(obj_dict)
    print(ser_obj)

    yaml_ser_func = yaml_parser.dumps(fa)
    yaml_des_func = yaml_parser.loads(yaml_ser_func)
    print(yaml_des_func(10))

    toml_ser_string = toml_parser.dumps(obj_dict)
   # toml_des_string = toml_parser.loads(toml_ser_string)
    toml_ser_func = toml_parser.dumps(fa)
    file = 'my_toml.toml'
    toml_parser.dump(fa, file)
    toml_parser.load(file)
    toml_des_func = toml_parser.loads(toml_ser_func)

   # print(toml_des_string)
    print(toml_ser_string)
    print(toml_ser_func)
    print(toml_des_func(10))


if __name__ == "__main__":
    main()
