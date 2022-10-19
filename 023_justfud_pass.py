import json
import os
 
TOKEN_SIZE = 100
START_ID = 0
OUTPUT_DIR = os.path.basename(__file__).split('.')[0]

NAME = "JustFUD Pass"
DESC = "Welcome to JustFUD Member System. Hope to enjoy in JustFUD. But it might be becoming something in the future. Who knows? 😏"
IMG = "https://diewland.github.io/special-eureka/assets/justfud-pass/{:03}.gif"
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
