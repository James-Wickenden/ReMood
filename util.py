
import os
import json

def convert_days():
    # first read folder and create json holding days data
    days_location = 'days_migrate/'
    days_dict = {}
    for filename in os.listdir(days_location):
        day = str.join('/', filename.split('.')[:-1])
        score = -1
        with open(days_location + filename, "r") as f:
            score = f.readline()
        days_dict[str.join('/', filename.split('.')[:-1])] = score

    # then write to json file
    with open("days_remood.json", "w") as days_remood_f:
        days_remood_f.write(
            json.dumps(days_dict, indent=4, sort_keys=True)
        )

