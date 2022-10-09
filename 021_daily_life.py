import json, os, glob, random
from pprint import pprint as pp
 
NAME = "Just Daily Life Jigsaw"
DESC = "A Jigsaw collection of one man daily life. Do you manage to hold the correct collection? Share to us at Jigsaw Family Discord. Enjoy!!!"
IMG = "https://diewland.github.io/special-eureka/assets/daily-life/{}"
ENGINE = "Jigsaw Engine"

SHUFFLE_TIME = 108
ASSET_DIR = './assets/daily-life/*.png'
OUTPUT_DIR = os.path.basename(__file__).split('.')[0]

NAME_MAPPER = [
    'Completed',
    '0700am',
    '0800am',
    '0900am',
    '1000am',
    '1100am',
    '1200pm',
    '1300pm',
    '1500pm',
    '1700pm',
    '1900pm',
    '2100pm',
    '2300pm',
]

# create bulklist
bulklist = [
    [ 'C1.jpg' ],
    [ 'C2.jpg' ],
    [ 'C3.jpg' ],
    [ 'C4.jpg' ],
    [ 'C5.jpg' ],
    [ 'C6.jpg' ],
    [ 'C7.jpg' ],
    [ 'C8.jpg' ],
    [ 'C9.jpg' ],
    [ 'C10.jpg' ],
    [ 'C11.jpg' ],
    [ 'C12.jpg' ],
]
bulklist += sorted([ [ os.path.basename(name) ] for name in glob.glob(ASSET_DIR) ])

# fname, name, collection, row, col
for b in bulklist:
    fname = b[0]
    if fname.startswith('C'):
        collection = NAME_MAPPER[0]
        vol = fname.split('.')[0][1:]
        name = "{} #{}".format(collection, vol)
        b += [ name, name, '1/1', '1/1' ]
    else: # DL_01_row-1-column-1.png
        (_, no, info) = fname.split('_')
        (_, row, _, col) = info.split('.')[0].split('-')
        no = int(no)
        row = int(row)
        col = int(col)
        collection = NAME_MAPPER[no]
        vol = ((row-1)*3) + col
        name = "{} #{}".format(collection, vol)
        b += [ name, collection, "{}/3".format(row), "{}/3".format(col) ]

# shuffle
for i in range(SHUFFLE_TIME):
    random.shuffle(bulklist)
    print('.', end='')
print('')

#pp(bulklist)
#print(len(bulklist))

metadata = {
  "name": "***",
  "description": DESC,
  "image": "***",
  "attributes": [
    {
      "trait_type": "Collection",
      "value": "***",
    },
    {
      "trait_type": "Row",
      "value": "***",
    },
    {
      "trait_type": "Column",
      "value": "***",
    },
  ],
  "compiler": ENGINE,
}

# build json + write to file
for id, (fname, name, collection, row, col) in enumerate(bulklist):
    metadata["name"] = name
    metadata["image"] = IMG.format(fname)
    metadata["attributes"][0]["value"] = collection
    metadata["attributes"][1]["value"] = row
    metadata["attributes"][2]["value"] = col

    #print(metadata)
    #print(name, collection, row, col, metadata["image"])

    # write file
    with open("./{}/{}.json".format(OUTPUT_DIR, id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
