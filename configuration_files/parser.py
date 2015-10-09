import json

with open("instruction.json") as instructions_file:
    instructions_data = json.load(instructions_file)
    #print(instructions_data)
    print(instructions_data['moveForward'])
