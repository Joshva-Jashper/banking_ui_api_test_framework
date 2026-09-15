import json

def read_json_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        el = json.load(file)
        for item in el:
            data.append(item.values())
    return data
