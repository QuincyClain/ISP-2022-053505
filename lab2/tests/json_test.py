import unittest
import json
import os
from my_factory import a_factory
from main import Person
from main import fa
from intermediate_parser import serialize_to_dict

class TestJson(unittest.TestCase):


    def test_json_obj(self):
        file = 'json_test.json'
        file_2 = 'my_json_test.json'
        self.test_obj = Person('Vlad', 19)
        self.test_obj_dict = self.test_obj.__dict__
        self.my_parser = a_factory.Factory()
        self.my_json_parser = self.my_parser.create_parser('JSON')
        self.json_string_object = json.dumps(self.test_obj_dict)
        self.my_json_string_object = self.my_json_parser.dumps(self.test_obj_dict)

        with open(file, 'w') as f:
            json.dump(self.test_obj_dict, f)
            f.close()

        with open(file, 'r') as f2:
            self.des_obj = json.load(f2)
            f2.close()
        os.remove(file)

        self.my_json_parser.dump(self.test_obj_dict, file_2)
        self.my_des_obj = self.my_json_parser.load(file_2)

        self.assertDictEqual(self.my_des_obj, self.des_obj)
        self.assertEqual(self.my_json_string_object, self.json_string_object)


    def test_json_loads_obj(self):
        self.test_obj = Person('Vlad', 19)
        self.test_obj_dict = self.test_obj.__dict__

        self.my_parser = a_factory.Factory()
        self.my_json_parser = self.my_parser.create_parser('JSON')

        self.my_json_string = self.my_json_parser.dumps(self.test_obj_dict)
        self.my_des_obj = self.my_json_parser.loads(self.my_json_string)

        self.json_string = json.dumps(self.test_obj_dict)
        self.json_des_obj = json.loads(self.json_string)

        self.assertDictEqual(self.my_des_obj, self.json_des_obj)


    def test_json_loads_func(self):
        self.my_parser = a_factory.Factory()
        self.my_json_parser = self.my_parser.create_parser('JSON')

        self.non_format_serialized_func = serialize_to_dict.serialize(fa)
        self.to_str = json.dumps(self.non_format_serialized_func)
        self.to_func = json.loads(self.to_str)
        self.to_to_func = serialize_to_dict.deserialize(self.to_func)

        self.my_json_ser_func = self.my_json_parser.dumps(fa)
        self.my_json_des_func = self.my_json_parser.loads(self.my_json_ser_func)

        self.a = self.to_to_func
        self.b = self.my_json_des_func

        self.assertEqual(self.a(10), self.b(10))


if __name__ == '__main__':
    unittest.main()