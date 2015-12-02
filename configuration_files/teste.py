import json
from execInstructions import ExecInstructions
from collections import OrderedDict

# Loads the Json file in a OrderedDict
parsed_json = json.load(open('instruction.json'), object_pairs_hook=OrderedDict)
#print json.dumps(parsed_json, indent=2)

# Instantiate class runner for instructions
instruction = ExecInstructions()

size = len(parsed_json)
i = 0
while i < size:
    # Execute inside loop instructions
    if(parsed_json.keys()[i] == 'loop'):
        for k in range(0, parsed_json.values()[i].get('loops')):
            for j in range(i, i+parsed_json.values()[i].get('instructions')):
                instruction.run(parsed_json.keys()[j], parsed_json.values()[j])

        # Jump to the next instruction outside the loop
        i = i+len(parsed_json.values()[i])

    else:
        # execute instruction
        instruction.run(parsed_json.keys()[i], parsed_json.values()[i])
        i += 1
