import json
from collections import OrderedDict

class Parser():

  def parseJson(self, jsonFile):
      # Loads the Json file in a OrderedDict
      parsed_json = json.load(open('instruction.json'), object_pairs_hook=OrderedDict)
      print json.dumps(parsed_json, indent=2)

      # Iterates through the json file
      size = len(parsed_json)
      for i in range(0, size):
          print parsed_json.keys()[i]
          print parsed_json.values()[i]
