from __future__ import print_function
import parse


class Item(object):
    def __init__(self, json):
        # Sanity check
        if 'type' not in json or json['type'] not in item_otypes:
            raise TypeError("Not an item type", json)

        parse.require_all(json, ('id', 'volume', 'weight'))

        self.itype_id = json['id']
        self.volume = parse.value_from(json, 'volume')
        self.weight = parse.value_from(json, 'weight')
        self.default_charges = parse.value_from(json, 'count', 1)

    def __repr__(self):
        return '<Item(%s)>' % self.itype_id



item_otypes = ['AMMO', 'ARMOR', 'BIONIC_ITEM', 'BOOK', 'COMESTIBLE', 'CONTAINER', 'GENERIC',
              'GUN', 'GUNMOD', 'TOOL', 'TOOL_ARMOR', 'VAR_VEH_PART']
objectifiers = dict.fromkeys(item_otypes, Item)

def objectify(categorized_json):
    obj_dict = {}
    for otype, objects in categorized_json.items():
        if otype not in objectifiers:
            continue
        objectify = objectifiers[otype]
        obj_dict[otype] = []

        for obj in objects:
            obj_dict[otype].append(objectify(obj))
    return obj_dict


all_json = parse.read_full_json("json/")
categories = parse.categorize(all_json)
json = parse.group(categories)
objects = objectify(categories)

items = {}

for otype in item_otypes:
    if otype not in objects:
        continue
    items.update({ item.itype_id: item for item in objects[otype]})
