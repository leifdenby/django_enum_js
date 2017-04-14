import json

class EnumWrapper:
    def __init__(self):
        self.registered_enums = {}

    def register_enum(self, enum_class):
        self.registered_enums[enum_class.__name__] = enum_class
        return enum_class

    def _enum_to_dict(self, enum_class):
        return dict([(k,v) for k,v in enum_class.__dict__.items() if not k[:2] == '__'])

    def _json_dump_enum(self, enum_class):
        return json.dumps(self._enum_to_dict(enum_class))

    def get_json_formatted_enums(self):
        data = {}
        for identifier, enum_content in self.registered_enums.items():
            data[identifier] = self._enum_to_dict(enum_content)

        return json.dumps(data)

enum_wrapper = EnumWrapper()
