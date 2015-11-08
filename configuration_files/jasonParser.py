import json
from pprint import pprint

# Text how to get the list of instructions

with open('instruction.json') as json_file:
    parsed_json = json.load(json_file)
    size = len(parsed_json)


    for i in range(0, size):
        print(parsed_json.keys()[i])
        print parsed_json.itervalues().next()
