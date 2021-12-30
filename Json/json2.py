import json
from os import stat

with open("states.json") as f:
    data = json.load(f)

for state in data['states']:
    del  state['abbreviation']

with open(file="new_states.json",mode="w") as jas:
    json.dump(data,jas, indent=2)


    

