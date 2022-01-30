import os
import json

### saving data in json file ###
def save_data(input): 
    fname = os.getcwd()+ "/static/sample_file.json"
    with open(fname , "r+") as file:
        data = json.load(file)

        data.append(input)
        with open(fname, mode='w') as f:
            f.write(json.dumps(data, indent=2))