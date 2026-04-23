import csv
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from array import *
import mplcursors
import numpy as np

filename = "test4.csv"
DataName = "DataName"
DataValue = "DataValue"
Removable = ","
data = []
data_number = 0

def output_char(split_types, nums, data_number):
    
    IDS_index = [i for i, x in enumerate(split_types) if x == "IDS"]
    if not IDS_index:
        print("no IDS value")
        return None

    VDS_index = [i for i, x in enumerate(split_types) if x == "VDS"]
    if not VDS_index:
        print("no vds")
        return None
    
    rdson_index = [i for i, x in enumerate(split_types) if x in ("Rdson", "Rdson\n", "RDSon", "RDSon\n")]
    if not rdson_index:
        print("no rdson")
        return None
    
    VGS_index = [i for i, x in enumerate(split_types) if x == "VGS"]
    if not VGS_index:
        print("no vgs")
        return None
    
    IDS = []
    VDS = []
    RDSon = []
    VGS = []
    resistance = "ohm"

    for i in range(data_number):
        for idx in IDS_index:
            IDS.append(nums[i][idx])
        for vdx in VDS_index:
            VDS.append(nums[i][vdx])
        for rdx in rdson_index:
            if rdx < len(nums[i]):
                RDSon.append(nums[i][rdx])
        for vgx in VGS_index:
            VGS.append(nums[i][vgx])
    
    VDS = np.array(VDS)
    IDS = np.array(IDS)
    VGS = np.array(VGS)
    VGS_values = np.unique(np.round(VGS, 10))
    colors = cm.viridis(np.linspace(0, 1, len(VGS_values)))
    print(VGS_values)

    for vgs, color in zip(VGS_values, colors):
        mask = np.isclose(VGS, vgs)
        if np.any(mask):
            actual_vgs = np.round(VGS[mask][0], 1)
            plt.plot(VDS[mask], IDS[mask], color = color, label=f"VGS={actual_vgs}V")
        print(actual_vgs)
            

    #plt.plot(VDS, IDS)

    cursor = mplcursors.cursor(hover=True)

    @cursor.connect("add")
    def on_add(sel):
        line = sel.artist
        #x, y = sel.target #if VDS IDS needed

        label = line.get_label()

        i = int(sel.index)

        sel.annotation.set_text(
            f"RDSon={RDSon[i]:.5f}{resistance} "
            f"{label}"
        )

    plt.xlabel("VDS (V)")
    plt.ylabel("IDS (A)")
    plt.legend()
    plt.show()


def IGSS(split_types, nums, data_number):

    IG_index = [i for i, x in enumerate(split_types) if x in ("IG", "IGabs")]
    if not IG_index:
        print("no ig")
        return None
    
    VGS_index = [i for i, x in enumerate(split_types) if x == "VGS"]
    if not VGS_index:
        print("no vgs")
        return None
    
def quadrant(split_types, nums, data_number):

    IDS_index = [i for i, x in enumerate(split_types) if x == "IDS"]
    if not IDS_index:
        print("no ids")
        return None
    
    VDS_index = [i for i, x in enumerate(split_types) if x == "VDS"]
    if not VDS_index:
        print("no vds")
        return None


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
