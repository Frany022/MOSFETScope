import csv
import numpy as np

def read_csv():
    data = []
    count = 0
    from_file = {
        "filename": "test3.csv",
        "DataName" : "DataName",
        "DataValue" : "DataValue"
    }
    with open(from_file["filename"], "r") as reader:
        csv_file = csv.reader(from_file["filename"], delimiter=',')
        for row in reader:
            if from_file["DataValue"] in row:
                data.append(row)
                count += 1
            elif from_file["DataName"] in row:
                data.append(row)
            else:
                pass
    reader.close
    type = parser(data, from_file)
    return data, count, type

def parser(data, from_file):
    for i in range(len(from_file["DataName"])):
        type = data[0].replace(from_file["DataName"] + "," + " ", "")
        type = type.split(", ")
    return type

def char():
    pass
