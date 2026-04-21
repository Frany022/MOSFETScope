import csv
import matplotlib.pyplot as plt
from array import *
import mplcursors


filename = "test2.csv"
DataName = "DataName"
DataValue = "DataValue"
Removable = ","
data = []
data_number = 0

def output_char(split_types, nums, data_number):
    if "IDS" in split_types:
        y_index = split_types.index("IDS")
    else:
        print("output char not available because no IDS")
        return None
    
    if "VDS" in split_types:
        x_index = split_types.index("VDS")
    else:
        print("output char not available because no VDS")
        return None
    
    if "Rdson" in split_types:
        rdson = split_types.index("Rdson")
    elif "Rdson\n" in split_types:
        rdson = split_types.index("Rdson\n")
    elif "RDSon" in split_types:
        rdson = split_types.index("RDSon")
    elif "RDSon\n" in split_types:
        rdson = split_types.index("RDSon\n")
    else:
        rdson = None
    IDS = []
    VDS = []
    RDSon = []
    
    for i in range(data_number):
        IDS.append(nums[i][y_index])
        VDS.append(nums[i][x_index])
        RDSon.append(nums[i][rdson])

    for i in range(data_number):
            RDSon[i] = RDSon[i] * 1000

    #print("rdson: ", RDSon)
    #print("VDS: ", x_axis)
    #plt.scatter(x_axis, y_axis, c=RDSon, cmap='viridis')
    #plt.colorbar(label="RDSon mohm")
    plt.plot(VDS, IDS)

    cursor = mplcursors.cursor(hover=True)
    @cursor.connect("add")
    def on_add(sel):
        i = int(round(sel.index))
        sel.annotation.set_text(f"RDSon={RDSon[i]:.4f} mohm")

    plt.xlabel("VDS (V)")
    plt.ylabel("IDS (A)")
    plt.legend("R mohm")
    plt.show()


def IGSS(split_types):
    if "IG" in split_types:
        y_index = split_types.index("IG")
    elif "IGabs" in split_types:
        y_index = split_types.index("IGabs")
    else:
        print("no IG, not able to plot")
        return None

    if "VGS" in split_types: 
        x_index = split_types.index("VGS")
    else: 
        x_index = None
    
    return y_index, x_index

def quadrant(split_types):
    if "IDS" in split_types:
        y_index = split_types.index("IDS")
    else:
        y_index = None

    if "VDS" in split_types:
        x_index = split_types.index("VDS")
    else:
        x_index = None

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


nums = [[0 for i in range(len(type_number))] for j in range(data_number)]

#data_number kettő lesz ebben az esteben és len(type_number) 4

for i in range(data_number + 1):
    if i == 0:
        continue
    value = data[i].replace(DataValue + Removable + " ", "")

    split_values = value.split(", ")

    nums[i - 1] = [float(x) for x in split_values]


split_types = type1.split(", ")

#print("split types: ", split_types) checking for the exact name
output_char(split_types, nums, data_number)
