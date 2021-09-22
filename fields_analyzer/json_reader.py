import json

def read_json_file(file_to_read) -> object:
    # Opening JSON file
    json_file = open(file_to_read, "r")
    # returns JSON object as dictionary
    json_data = json.load(json_file)

    #print(json_data[0]["pid"])

    # Closing file
    json_file.close()

    return json_data