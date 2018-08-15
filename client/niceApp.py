import hashlib
import json
import random
import sys
import time

import requests

sys.path.append(r'C:\Users\saad\Desktop\Nerding\PyEnv\omaha\omahasim\server')

UPDATE_PATH = r'C:\Users\saad\Desktop\Nerding\PyEnv\omaha\omahasim\client\update.json'
def updateApp():
    print("Connecting to update server...")
    r = requests.get('http://localhost:8888')
    with open(UPDATE_PATH, 'r') as readit:
        read = json.load(readit)
        ORIGINAL_HASH = read["HASH"]
        print(f"Original hash is : {ORIGINAL_HASH}")
        BUILD = read["BUILD"]
        print(f"BUILD : {BUILD}")
    print(f"server update : {r.text}")
    if ORIGINAL_HASH == r.text:
        print(f"Your app is up to date, last build is {BUILD}")
    else:
        print("There is a new update !")
        read["HASH"] = r.text
        read["BUILD"] += 1
        BUILD = read["BUILD"]
        with open(UPDATE_PATH, 'w') as saveit:
            json.dump(read, saveit)
        print("Update successful !")
        print(f"new Build #{BUILD}")

if __name__ == "__main__":
    updateApp()

