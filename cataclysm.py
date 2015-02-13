from __future__ import print_function
import parse

all_json = parse.read_full_json("json/")

object_types = set((obj['type'] for obj in all_json))

# Most things have an "id" they use as keys. This holds overrides:
id_key_exceptions = {"BULLET_PULLING": "bullet",
                     "MONSTER_FACTION": "name",
                     "construction": None,
                     "dream": None,
                     "hint": None,
                     "lab_note": None,
                     "mapgen": None,
                     "material": "ident",
                     "monstergroup": "name",
                     "profession": "ident",
                     "recipe": None, # technically, "result", but it's non-unique
                     "scenario": "ident",
                     "skill": "ident",
                     "snippet": None,
                     "speech": None,
                     "start_location": "ident",
                     "tutorial_messages": None}


item_types = ["AMMO", "ARMOR", "BIONIC_ITEM", "BOOK", "COMESTIBLE", "CONTAINER", "GENERIC",
              "GUN", "GUNMOD", "ITEM_CATEGORY", "TOOL", "TOOL_ARMOR", "VAR_VEH_PART"]

json = {}

for t in object_types:
    key_name = 'id'
    if t in id_key_exceptions:
        if id_key_exceptions[t] is None:
            continue # Don't even bother with these guys
        key_name = id_key_exceptions[t]

    json[t] = { obj[key_name]: obj for obj in all_json if obj['type'] == t and key_name in obj }

    if not json[t]:
        print("WARN: Can't make sense of these", t, "objects. Here's what one looks like:",
              repr((obj for obj in all_json if obj['type'] == t).next()))

