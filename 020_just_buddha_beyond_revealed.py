import json, os, glob, random
from pprint import pprint as pp
 
NAME = "Just Buddha Beyond"
DESC = 'What is the future world? Will religion influent people mind and living expectation. What will be beyond Buddha or Buddha beyond everthing. "Our NFT will be last for worship forever, Rafael" No Art, No Road, No Utilities, Part of Just Metaverse'
IMG = "https://diewland.github.io/special-eureka/assets/bdb/{}"
ENGINE = "Jigsaw Engine"

RARITY_MAPPING = {
    'C':    'Common',
    'UC':   'Uncommon',
    'R':    'Rare',
    'UR':   'Ultra Rare',
}

SHUFFLE_TIME = 108
ASSET_DIR = './assets/bdb/*.png'
OUTPUT_DIR = os.path.basename(__file__).split('.')[0]
START_ID = 0

# craft + shuffle input
bulklist = [ os.path.basename(name) for name in glob.glob(ASSET_DIR) ]
for i in range(SHUFFLE_TIME):
    random.shuffle(bulklist)
    print('.', end='')
print('')


# build json + write to file
for id, fname in enumerate(bulklist):
    rcode = fname.split(' ')[0]
    rarity = RARITY_MAPPING[rcode]
    metadata = {
      "name": "***",
      "description": DESC,
      "image": "***",
      "attributes": [
        {
          "trait_type": "Rarity",
          "value": rarity,
        },
      ],
      "compiler": ENGINE,
    }
    metadata["name"] = "{} #{}".format(NAME, id)
    metadata["image"] = IMG.format(fname)

    #print("{}\t{}\t{}".format(fname, rarity, metadata['image']))

    # write file
    with open("./{}/{}.json".format(OUTPUT_DIR, START_ID + id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
