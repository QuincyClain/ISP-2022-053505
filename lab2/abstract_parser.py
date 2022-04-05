from abc import abstractclassmethod, abstractmethod


class AbstractParser:
    def dump(self, obj):
        ...
    @abstractmethod
    def dumps(self, obj):
        ...
    def load(obj):
        pass
    def loads(obj):
        pass
