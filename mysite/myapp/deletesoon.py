import json 


with open("reports/"+'25533c7055295127646cfa5e560df2e0' + ".json", encoding="utf-8") as jsonfile:
    json_obj = json.load(jsonfile)
    print(json_obj)