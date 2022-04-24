import unittest
import os
from my_factory import a_factory
from main import Person
import qtoml
from main import fa
from intermediate_parser import serialize_to_dict


class TestToml(unittest.TestCase):

    def test_toml_obj(self):
        file = 'toml_test.toml'
        file_2 = 'my_toml_test.toml'
        obj = Person('Vlad', 19)
        obj_to_dict = obj.__dict__

        self.my_parser = a_factory.Factory()
        self.my_toml_parser = self.my_parser.create_parser('TOML')

        with open(file, 'w') as f:
            qtoml.dump(obj_to_dict, f)
            f.close()
        with open(file, 'r') as f2:
            self.des_obj = qtoml.load(f2)
            f2.close()
        os.remove(file)
        self.my_toml_parser.dump(obj_to_dict, file_2)
        self.my_des_obj = self.my_toml_parser.load(file_2)

        self.assertDictEqual(self.des_obj, self.my_des_obj)


    def test_toml_func(self):
        self.my_parser = a_factory.Factory()
        self.my_toml_parser = self.my_parser.create_parser('TOML')

        self.f_to_d = serialize_to_dict.serialize(fa)
        self.toml_func_string = qtoml.dumps(self.f_to_d)
        self.toml_des_dict = qtoml.loads(self.toml_func_string)
        self.toml_des_func = serialize_to_dict.deserialize(self.toml_des_dict)

        self.my_toml_func_string = self.my_toml_parser.dumps(fa)
        self.my_toml_des_func = self.my_toml_parser.loads(self.my_toml_func_string)

        self.assertEqual(self.toml_des_func(10), self.my_toml_des_func(10))


if __name__ == '__main__':
    unittest.main()