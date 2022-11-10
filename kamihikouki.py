import json
import os
 
TOKEN_SIZE = 256
START_ID = 0
OUTPUT_DIR = os.path.basename(__file__).split('.')[0]

NAME = "Kamihikouki ✈️"
DESC = "Kamihikouki means a Paper Plane. ☁️ Life is like a Paper Plane. It doesn't matter where you come from. All that matters is where you are going and where you have been.🐈 No Roadmap, No Utility, No Art, Just Flyyyy✈️"
IMG = "https://diewland.github.io/special-eureka/assets/kamihikouki.gif"
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
