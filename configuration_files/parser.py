import json

class Parser():

  def parseJson(Jsonfile):
    with open("instruction.json") as instructions_file:
      instructions_data = json.load(instructions_file)
      print(Jsonfile)
      print(instructions_data)
    return 
