import json
import os
 
TOKEN_SIZE = 100
START_ID = 0
OUTPUT_DIR = os.path.basename(__file__).split('.')[0]

NAME = "Crypto Robo"
DESC = "100 Pure Art of Super Cool Robots. Now available on Arbitrum One L2 Blockchain. This collection was generated by AI with love 🤖❤️"
IMG = "https://diewland.github.io/special-eureka/assets/crb_unrevealed.gif"
ATTRS = [
    # standard
    #{
    #  "trait_type": "Collection",
    #  "value": NAME, 
    #},
    # custom
    #{
    #  "trait_type": "Rarity",
    #  "value": "Unrevealed",
    #},
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