import csv
import matplotlib.pyplot as plt
from array import *


filename = "test1.csv"
DataName = "DataName"
DataValue = "DataValue"
Removable = ","
data = []
data_number = 0

def output_char(split_types):
    if "IDS" in split_types:
        y_index = split_types.index("IDS")
    else:
        print("output char not available because no IDS")
    if "VDS" in split_types:
        x_index = split_types.index("VDS")
    else:
        print("output char not available because no VDS")
    if "Rdson" in split_types:
        rdson = split_types.index("Rdson")
    elif "Rdson\n" in split_types:
        rdson = split_types.index("Rdson\n")
    return y_index, x_index, rdson

def IGSS(split_types):
    y_index = split_types.index()
    x_index = split_types.index()
    return y_index, x_index

def quadrant(split_types):
    y_index = split_types.index()
    x_index = split_types.index()
    return y_index, x_index


with open(filename, 'r') as reader:
    csv_file = csv.reader(filename, delimiter=',')
    for row in reader:
        if DataValue in row:
            data.append(row)
            data_number += 1
        elif DataName in row:
            data.append(row)
        else:
            pass
reader.close

for type1 in range(len(DataName)): 
    type1 = data[0].replace(DataName + Removable + " ", "")



type_number = [y for y in type1.split("," + " ")]

print(type_number)

nums = [[0 for i in range(len(type_number))] for j in range(data_number)]
print("empty 2d array:", nums)

#data_number kettő lesz ebben az esteben és len(type_number) 4

for i in range(data_number + 1):
    if i == 0:
        continue
    print(i)
    value = data[i].replace(DataValue + Removable + " ", "")

    split_values = value.split(", ")

    nums[i - 1] = [float(x) for x in split_values]

print(nums)
print(type1)

split_types = type1.split(", ")

#print("split types: ", split_types) checking for the exact name

y_index, x_index, Rdson = output_char(split_types)

print("y index: ", y_index)
print("x index: ", x_index)
print("rdson: ", Rdson)



