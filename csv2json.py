import csv
import json

class FileModification:
    def csv_to_json(csvFilePath):
        jsonArray = []

        with open(csvFilePath, encoding= 'utf-8') as csvf:
            #load csv file data
            csvReader = csv.DictReader(csvf, skipinitialspace=True, delimiter=",")

            #convert each row into a python dict
            for row in csvReader:
                
                jsonArray.append(row)

            jsonString = json.dumps(jsonArray, indent= 4)
            print(jsonString)

# path = "C:/Users/Daniel/Desktop/"   
# myfile = path + "Transactions_transaction_csv_report_138157649.csv"  
denirocsvFilePath = 'deniro.csv'
mlbcsvFilePath = 'mlb_players.csv'
#csvFilePath = myfile
# FileModification.csv_to_json(denirocsvFilePath)
FileModification.csv_to_json(mlbcsvFilePath)