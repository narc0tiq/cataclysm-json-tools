import os
import json

def json_files(path='.'):
    jsons = []
    for root, dirs, files in os.walk(path, followlinks=True):
        jsons.extend((os.path.join(root, f) for f in files if f.endswith('.json')))

    return jsons

def read_full_json(path):
    all_in_one = []
    for fname in json_files(path):
        with open(fname) as fp:
            all_in_one.extend(json.load(fp))

    return all_in_one
