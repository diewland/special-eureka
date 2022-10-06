import json
import os
 
TOKEN_SIZE = 2922
START_ID = 0
OUTPUT_DIR = os.path.basename(__file__).split('.')[0]

NAME = "Just Tu naja 🌝"
DESC = "Website link --> Link for minting page, still active A NFT memorial to honor the day 30th September 2022 when goodness can overcome any obstacles. 2922 nft represents no of days in eight years. It will be our good luck charm to whom has a good deed. For the sake of greater good, we shall celebrate together. No road map, no utility, no art, just a good luck charm."
IMG = "https://diewland.github.io/special-eureka/assets/jtnj.png"
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
