import json
import os
 
TOKEN_SIZE = 108
START_ID = 0
OUTPUT_DIR = os.path.basename(__file__).split('.')[0]

NAME = "Just Buddha Beyond"
DESC = 'What is the future world? Will religion influent people mind and living expectation. What will be beyond Buddha or Buddha beyond everthing. "Our NFT will be last for worship forever, Rafael" No Art, No Road, No Utilities, Part of Just Metaverse'
IMG = "https://diewland.github.io/special-eureka/assets/jbb.gif"
ATTRS = [
    # standard
    #{
    #  "trait_type": "Collection",
    #  "value": NAME, 
    #},
    # custom
    {
      "trait_type": "Rarity",
      "value": "Unrevealed",
    },
]
ENGINE = "Jigsaw Engine"

metadata = {
  "name": "***",
  "description": DESC,
  "image": "***",
  "attributes": ATTRS,
  "compiler": ENGINE,
}

for id in range(0, TOKEN_SIZE):
    metadata["name"] = "{} #{}".format(NAME, id)
    metadata["image"] = IMG.format(id)
    with open("./{}/{}.json".format(OUTPUT_DIR, START_ID + id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
