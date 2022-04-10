from abc import abstractclassmethod, abstractmethod


class AbstractParser:
    @abstractmethod
    def dump(self, obj):
        ...
    @abstractmethod
    def dumps(self, obj):
        ...
    @abstractmethod
    def load(self, file):
        ...
    @abstractmethod
    def loads(self, obj):
        ...
