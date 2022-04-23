import json
from os import path

BASE_PATH = path.abspath(path.dirname(__file__))

with open(path.join(BASE_PATH, 'conf.json'), 'r') as conf_json:
    _config = json.load(conf_json)

assert 'quarters_path' in _config.keys(),\
    'Required entry, "quarters_path, " missing in conf.json'

QUARTERS_PATH = _config['quarters_path']
