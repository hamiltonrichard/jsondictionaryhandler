import json
import jsonpickle
import sys
""" 
JsonDictHandler

Class to convert dictionaries to json and back again.
This includes writing the JSON to pickle files 

"""
class JsonDictHandler:

# Convert a dictionary to JSON
    def dictionary_to_json(self, input_dict):
        return json.dumps(input_dict)

# Pickle a JSON object
    def pickle_json_to_file(self, obj, filename):
        with open(filename, 'w') as file:
            json_str = jsonpickle.encode(obj)
            file.write(json_str)

# Read a picked json file and return it
    def pickle_file_to_json(self, filename):
        with open(filename, 'r') as file:
            json_str = file.read()
            obj = jsonpickle.decode(json_str)
            return obj
#  take commandline args and create a dictionary which then can be converted. 
    def args_to_dict(self):
        result = {}
        for arg in sys.argv[1:]:
            key, value = arg.split('=')
            result[key] = value
        return result

"""
# Example usage:
if __name__ == "__main__":
    handler = JsonHandler()
    my_dict = {"name": "John", "age": 30}
    json_str = handler.dictionary_to_json(my_dict)
    print(json_str)
    handler.json_to_file(my_dict, "data.json")
    loaded_dict = handler.file_to_json("data.json")
    print(loaded_dict)
    args_dict = handler.args_to_dict()
    print(args_dict)
"""