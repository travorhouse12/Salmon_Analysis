import csv
import json
 
csvFilePath = 'salmon_pre_processed.csv'
jsonFilePath = 'salmon_processed.json'

data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        Brood_Year = rows['Brood_Year']
        data[Brood_Year] = rows
        
with open(jsonFilePath, 'w') as jsonFile:
         jsonFile.write(json.dumps(data, indent=4))