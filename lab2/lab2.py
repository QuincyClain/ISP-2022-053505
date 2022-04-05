import json
import factory

a = 10
b = 20
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        str_age = str(self.age)
        print("Hello my name is " + self.name + " and I'm " + str_age + " years old.")


#test func
def fact(n):
    print(a)
    print(b)
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def Sum_number():
    print(a)
    print(b)
    return a+b


def main():
    #json to dict
    x =  '{ "name":"Vlad", "age":19, "city":"Minsk"}'
    y = json.loads(x)
    print(y["name"], y["age"], y["city"])


    obj = Person("Vlad", 19)
    obj_dict = obj.__dict__

    serializer = factory.Serializer_factory()
    json_parser = serializer.create_serializer('JSON')


    #json_string = json.dumps(obj_dict)
    json_parser_string = json_parser.dumps(obj_dict)
    json_parser_func = json_parser.dumps(fact)

    json_parser.dump(fact, 'serialize.txt')
    json_parser.dump(obj_dict, 'serialize2.txt')

    print("JSON: ")
    #print(json_string)
    print(json_parser_string)
    print(json_parser_func)


    print("YAML: ")
 

    obj_dict = Person(obj_dict["name"], obj_dict["age"])

    if isinstance(obj_dict, Person):
        print(True)
    else:
        print(False)
    
    

if __name__ == "__main__":
    main()
