import csv
import json
 
csvFilePath = 'salmon_pre_processed_copy.csv'
jsonFilePath = 'salmon_pre_processed.json'

data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        ID = rows['ID']
        data[ID] = rows
        
with open(jsonFilePath, 'w') as jsonFile:
         jsonFile.write(json.dumps(data, indent=4))