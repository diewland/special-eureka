import json
import os
 
TOKEN_SIZE = 10_000
START_ID = 0
OUTPUT_DIR = os.path.basename(__file__).split('.')[0]

NAME = "One_collection 💯🔴"
DESC = "-Free Mint, place ur address in the linked twitter. -Sell low price in ETH and OP. -Zero royalty for min fee for re-sell. Want to do activities in Quix. Have all in here.!!! -Or mint from smart contract directly without WL required at https://optimistic.etherscan.io/token/0x5f817754Ad8bb4bCcEEc1fB5342658b3779423b9#writeContract"
IMG = "https://diewland.github.io/special-eureka/assets/one-profile.gif"
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
