These are some simple tools for fooling around with the JSON-format data files
included in [Cataclysm: Dark Days Ahead](http://cataclysmdda.com/).

The tools are written in [Python](http://python.org/) and have no further
dependencies at this time.


## License ##

The source code included is Copyright 2015 Octav "narc" Sandulescu. It is
licensed under the [MIT license](http://opensource.org/licenses/mit-license.html),
available in this package in the file [LICENSE.md](LICENSE.md).


## Dependencies ##

All the packages used so far are built-ins. The code is written against Python
2.7.6. No attempt has yet been made to bring it to Python 3, though the
conversion is expected to be trivial.


## Installing ##

There are no installable tools as yet, only some modules that can be imported.
Just have them somewhere in your PYTHONPATH and you're good to go.

The cataclysm module at present assumes the Cataclysm:DDA data files are
available in a subdirectory (or symlink) named `json`. It will scan recursively
for files with names ending in '.json' within this directory.


## Running the code ##

At present, the entry point is `cataclysm.py`; a simple `import cataclysm` will
give you everything, which is not very much:

- you can access a categorized breakdown of JSON objects from the
`cataclysm.json` member:

```
>>> import cataclysm
>>> cataclysm.json['AMMO']['9mm']
{u'weight': 7, u'color': u'yellow', u'id': u'9mm', u'to_hit': 0, u'damage': 18, u'dispersion': 150,
 u'type': u'AMMO', u'price': 2400, u'description': u'9 millimeter parabellum is generally regarded 
as the most popular handgun cartridge and used by the majority of US police forces.  It is also a v
ery popular round in sub-machine guns.', u'symbol': u'=', u'material': u'steel', u'ammo_type': u'9m
m', u'cutting': 0, u'recoil': 195, u'effects': [u'COOKOFF'], u'count': 50, u'volume': 1, u'pierce':
 2, u'casing': u'9mm_casing', u'name': u'9mm', u'bashing': 1, u'range': 14, u'name_plural': u'9mm'}
```

Of necessity, some object types are left out (namely, those that do not have
unique keys; this includes recipes).

- you can also obtain the uncategorized array comprising all the JSON objects
from the `cataclysm.all_json` member:

```
>>> import cataclysm
>>> cataclysm.all_json[0]
{u'category': u'MUTCAT_LIZARD', u'messages': [u'You have a strange dream about lizards.', u'Your dr
eams give you a strange scaly feeling.'], u'strength': 1, u'type': u'dream'}
```

This includes objects not in the `json` member.


## Trivia ##

At the time of this writing, the Cataclysm data files contained 390 GENERIC
items and 626 COMESTIBLE ones.
