import os
import json

# What object types do we understand?
# This is an exhaustive list, as far as the library is concerned: if it's not
# here, it doesn't exist.
object_types = ['AMMO', 'ARMOR', 'BIONIC_ITEM', 'BOOK', 'BULLET_PULLING',
                'COMESTIBLE', 'CONTAINER', 'GENERIC', 'GUN', 'GUNMOD',
                'ITEM_CATEGORY', 'MONSTER', 'MONSTER_FACTION', 'SPECIES',
                'TOOL', 'TOOL_ARMOR', 'VAR_VEH_PART', 'ammunition_type',
                'bionic', 'construction', 'effect_type', 'faction',
                'furniture', 'item_action', 'item_group', 'martial_art',
                'material', 'monstergroup', 'mutation', 'npc',
                'overmap_special', 'overmap_terrain', 'profession', 'recipe',
                'recipe_category', 'region_settings', 'scenario', 'skill',
                'start_location', 'technique', 'terrain', 'tool_quality',
                'trap', 'vehicle', 'vehicle_part']


# Most things have an "id" they use as keys. This holds overrides:
id_key_exceptions = {'BULLET_PULLING': 'bullet',
                     'MONSTER_FACTION': 'name',
                     'construction': None,
                     'material': 'ident',
                     'monstergroup': 'name',
                     'profession': 'ident',
                     'recipe': None, # technically, 'result', but it's non-unique
                     'scenario': 'ident',
                     'skill': 'ident',
                     'start_location': 'ident'}


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


def categorize(all_json):
    categorized_json = {}
    for t in object_types:
        categorized_json[t] = [obj for obj in all_json if obj['type'] == t]

    return categorized_json


def group(categorized_json):
    grouped_json = {}
    for t in categorized_json.keys():
        key_name = 'id'
        if t in id_key_exceptions:
            if id_key_exceptions[t] is None:
                continue # Explicitly marked as "do not group"
            key_name = id_key_exceptions[t]

        grouped_json[t] = { obj[key_name]: obj for obj in categorized_json[t] if key_name in obj }

    return grouped_json


def categorize_and_group(all_json):
    return group(categorize(all_json))


def value_from(json, key, default=None):
    value = default
    if key in json:
        value = json[key]
    return value

def require_all(json, keys):
    """ Require that the given dict-from-json-object contains all given keys """
    for k in keys:
        if k not in json:
            return False
    return True

def require_any(json, keys):
    """ Require that the given dict-from-json-object contains at least one of the given keys. """
    for k in keys:
        if k in json:
            return True
    return False
