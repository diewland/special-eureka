import json
import os
 
TOKEN_SIZE = 10_000
START_ID = 0
OUTPUT_DIR = os.path.basename(__file__).split('.')[0]

NAME = "Just Meaw 😺"
DESC = "Just Meaw now Rebranded to Just Meaw USD Real world Money used in Meawtaverse Project🌎 You Can Buy Anything 🏡🚕🥬🍷💎🛸🗿🎡🏓🔧 If Anyone Accept Just Meaw USD💰 even L❤️VE 10,000/10,000 No $, Just Meaw UsD"
IMG = "https://diewland.github.io/special-eureka/assets/just_meaw.gif"
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
