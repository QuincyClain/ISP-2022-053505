from my_factory.a_factory import *
from console_args.my_args import ArgParse


class CallMethods:

    def init_parser(filename: str):
        parser = Factory()
        type_parser = None
        filetype = filename.lower().split('.')[-1]
        if filetype == 'json':
            type_parser = parser.create_parser('JSON')
        elif filetype == 'yml':
            type_parser = parser.create_parser('YAML')
        elif filetype == 'toml':
            type_parser = parser.create_parser('TOML')
        return type_parser

    def dump(obj, filename: str):
        my_parser = CallMethods.init_parser(filename)
        if my_parser is None:
            print('Incorrect filetype')
        my_parser.dump(obj, filename)
        print('Success')
        return filename

    def load(filename: str):
        my_parser = CallMethods.init_parser(filename)
        if my_parser is None:
            print('Incorrect filetype')
        obj = my_parser.load(filename)
        print('Success')
        return obj

    @staticmethod
    def convert():
        global obj
        if ArgParse.load_file is not None:
            obj = CallMethods.load(''.join(ArgParse.load_file()))

        if ArgParse.dump_file is not None:
            CallMethods.dump(obj, ''.join(ArgParse.dump_file()))


