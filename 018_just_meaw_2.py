import json
import os
 
TOKEN_SIZE = 10_000
START_ID = 0
OUTPUT_DIR = os.path.basename(__file__).split('.')[0]

NAME = "Just Meaw Limitless 🔥"
DESC = "Season 2 is now released!. Let mint at https://qx.app/launch/0x925Ef88660E810b7360972909499D0f709E8F4e3 or click at website link."
IMG = "https://diewland.github.io/special-eureka/assets/just_meaw_2.gif"
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
