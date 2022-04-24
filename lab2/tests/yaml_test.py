import unittest
import yaml
import os
from yaml import Loader
from my_factory import a_factory
from main import Person
from main import fa
from intermediate_parser import serialize_to_dict


class TestYaml(unittest.TestCase):

    def test_yaml_obj(self):
        file = 'yaml_dump_test.yml'
        file_2 = 'my_yaml_dump_test.yml'
        obj = Person('Vlad', 19)
        obj_dict = obj.__dict__
        self.my_parser = a_factory.Factory()
        self.my_yaml_parser = self.my_parser.create_parser('YAML')
        with open(file, 'w') as f:
            f.write(yaml.safe_dump(obj_dict))
            f.close()
        stream = open(file, 'r')
        self.des_obj = yaml.load(stream, Loader=Loader)
        stream.close()
        os.remove(file)
        self.my_yaml_parser.dump(obj_dict, file_2)
        self.my_des_obj = self.my_yaml_parser.load(file_2)
        os.remove(file_2)

        self.assertDictEqual(self.des_obj, self.my_des_obj)

    def test_yaml_func(self):
        file = 'yaml_func_test.yml'
        self.my_parser = a_factory.Factory()
        self.my_yaml_parser = self.my_parser.create_parser('YAML')
        f_to_d = serialize_to_dict.serialize(fa)
        with open(file, 'w') as f:
            f.write(yaml.safe_dump(f_to_d))
            f.close()
        stream = open(file, 'r')
        self.des_dict = yaml.load(stream, Loader=Loader)
        self.des_func = serialize_to_dict.deserialize(self.des_dict)
        stream.close()
        os.remove(file)
        self.my_yaml_ser_func = self.my_yaml_parser.dumps(fa)
        self.my_des_func = self.my_yaml_parser.loads(self.my_yaml_ser_func)

        self.assertEqual(self.my_des_func(10), self.des_func(10))


if __name__ == '__main__':
    unittest.main()
