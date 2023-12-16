import yaml
from yaml import Loader, Dumper

# @title Utility function to make nested objects JSON serializable
class DICTIONARY(dict):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if isinstance(v, dict):
                self.__dict__[k] = DICTIONARY(**v)
            else:
                self.__dict__[k] = v

        super(DICTIONARY, self).__init__(self.__dict__)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def keys(self):
        return list(self.__dict__.keys())

class CONFIG(DICTIONARY):
    def __init__(self, config_file='docbot/config/config.yaml', **kwargs):
        with open(config_file) as f:
            config = yaml.load(f, Loader=Loader)

        for key, val in kwargs.items():
            config[key] = val

        super(CONFIG, self).__init__(**config)

    def to_json(self):
        out_dict = {}
        for k, v in self.__dict__.items():
            if isinstance(v, CONFIG):
                out_dict[k] = v.to_json()
            elif isinstance(v, list):
                li = []
                for i in v:
                    if isinstance(i, CONFIG):
                        li.append(i.to_json())
                    else:
                        li.append(i)
                out_dict[k] = li
            else:
                out_dict[k] = v
        return out_dict

    def save(self, path='docbot/config/out.yaml'):
        with open(path, 'w') as f:
            yaml_obj = self.to_json()
            Dumper.ignore_aliases = lambda *args: True
            yaml.dump(yaml_obj, f, Dumper=Dumper)
