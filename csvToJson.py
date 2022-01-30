import csv
import json

with open("UN_Comtrade_Commodity_Classifications_HS_Codes_2017_version.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    print(reader)
    data = []
    
    for row in reader:
        data.append({"classification" : row[0], "code": row[1], "description": row[2], "parent_code": row[3], "level": int(row[4]), "isLeaf": row[5]})
        
        
       
with open("UN_Hscode.json", "w") as f:
    json.dump(data, f, indent=4)