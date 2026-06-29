import os
import json

pathh = os.path.join("data","karvand.json")

if not os.path.exists("data"):
    os.mkdir("data")

if not os.path.exists(pathh):
    with open (pathh, "w") as file:
        json.dump({}, file, indent=4)
