from types import FunctionType, CodeType
import json_class

class Serializer_factory:
    def create_serializer(self, format):
        parser = None
        if format == "JSON":
            parser = json_class.JSON()
            return parser
        else:
            raise ValueError(format)

#factory

