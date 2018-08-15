'''
Supposed this is the google engineer who adds new things to Chrome.
Supposed his name is Ben, Ben will work often to make Chrome up to date.
Each new update is a random word that we suppose is real code,
and after each feature added, the server will generate a new link
with a version. That's all we should know here.
'''
import datetime
import json
import random

# Change this to yours
UPDATE_PATH = r'C:\Users\saad\Desktop\Nerding\PyEnv\omaha\omahasim\server\updateHistory\updates.json'

# Developping a feature here and push it to json file
def dev(drinkCoffee):

    ACTIONS = ['added', 'deleted', 'fixed', 'modified',
           'deprecated', 'canceled', 'expanded', 'reviewed']
    FEATURES = ['Plugin', 'Section', 'Code', 'Bug', 'Tabs', 'Binary', 'Display']

    # read json file for updates info
    with open(UPDATE_PATH, 'r') as upd:
        save = json.load(upd)
        a = random.choice(ACTIONS)
        f = random.choice(FEATURES)
        save["updates"]["previousUpdate"].append(save["updates"]["new"])
        save["updates"]["new"] = a + f
        save["updates"]["build"] = save["updates"]["build"] + 1
        save["updates"]["date"] = str(datetime.date.today())
    if drinkCoffee:
        with open(UPDATE_PATH, 'w') as upd:
            json.dump(save, upd)
        return {"Update released": a + f}
    else:
        return "Ben is afk"

dev(True)


