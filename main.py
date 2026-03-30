import csv
import matplotlib.pyplot as plt
from array import *
import ast

filename = "test1.csv"
DataName = "DataName"
DataValue = "DataValue"
Removable = ","
data = []
data_number = 0

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

print(data[1])
print(data[2])
for i in range(data_number + 1):
    if i == 0:
        continue
    print(i)
    value = data[i].replace(DataValue + Removable + " ", "")

    split_values = value.split(", ")

    nums[i - 1] = [float(x) for x in split_values]

print(nums)
print(type1)
