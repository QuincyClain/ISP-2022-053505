from abc import abstractmethod


class AbstractParser:
    @abstractmethod
    def dump(self, obj, file):
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
