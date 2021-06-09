import json


class JsonWriter:
    def __init__(self, filepath, indent=None):
        self.filepath = filepath
        self.lines = 0
        with open(filepath, 'w') as f:
            f.write('[')

    def write_dict(self, dct: dict) -> None:
        jsn = json.dumps(dct)
        with open(self.filepath, 'a') as f:
            f.write(',\n') if self.lines else f.write('\n')
            f.write(jsn)
        self.lines += 1

    def close(self):
        with open(self.filepath, 'a') as f:
            f.write('\n')
            f.write(']')
