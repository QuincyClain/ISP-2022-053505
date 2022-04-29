import argparse


class ArgParse:
    @staticmethod
    def run_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument('-l', '--load', dest='l', nargs='+')
        parser.add_argument('-d', '--dump', dest='d', nargs='+')
        parser.add_argument('-c', '--config', dest='c', nargs='?')
        return parser.parse_args()

    @staticmethod
    def load_file() -> list[str]:
        args = ArgParse.run_parser()
        return args.l

    @staticmethod
    def dump_file() -> list[str]:
        args = ArgParse.run_parser()
        return args.d

    @staticmethod
    def args_config(config: str) -> list[str]:
        try:
            file = open(config, 'r')
            get_conf = file.read()
        except Exception as e:
            print(e)
        finally:
            file.close()
            return get_conf.split('\n')

    @staticmethod
    def get_args():
        args = ArgParse.run_parser()
        if args.c is not None:
            args.d, args.l = ArgParse.args_config()
        return args.d, args.l
