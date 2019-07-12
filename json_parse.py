import json

with open("./dummy1.json", "r") as json_file:
    dict_dummy = json.load(json_file)
    # print(dict_dummy)

    for entry in dict_dummy:
        if "email" and "name" in entry.keys():
            print(entry["name"], ":", entry["email"])
        else:
            print("Invalid data:", entry)




