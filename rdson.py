import numpy as np
import mplcursors
import matplotlib.pyplot as plt
import matplotlib.cm as cm

for_rdson = {
    "IDS" : "IDS",
    "VDS" : "VDS",
    "RDSon" : "rdson",
    "VGS" : "VGS"
}

def parser(data, from_file, count):
    for i in range(len(from_file["DataName"])):
        types = data[0].replace(from_file["DataName"] + "," + " ", "")
        types = types.split(", ")
    nums = [[0 for i in range(len(types))] for j in range(count)]
    for i in range(count + 1):
        if i == 0:
            continue
        values = data[i].replace(from_file["DataValue"] + "," + " ", "")
        values = values.split(", ")
        nums[i - 1] = [float(x) for x in values]

        max_len = max(len(row) for row in nums)
        for row in nums:
            while len(row) < max_len:
                row.append(0)

    char(count, types, nums)

def char(count, types, nums):

    IDS_index = [i for i, x in enumerate(types) if x == for_rdson["IDS"]]
    VDS_index = [i for i, x in enumerate(types) if x == for_rdson["VDS"]]
    RDSon_index = [i for i, x in enumerate(types) if x.lower() == for_rdson["RDSon"] or "rdson\n"]
    VGS_index = [i for i, x in enumerate(types) if x == for_rdson["VGS"]]

    if not IDS_index:   print("No IDS for char");   return
    if not VDS_index:   print("No VDS for char");   return
    if not RDSon_index: print("No rdson for char"); return
    if not VGS_index:   print("No vgs for char");   return

    nums = np.array(nums)

    IDS = nums[:count, IDS_index].flatten()
    VDS = nums[:count, VDS_index].flatten()
    RDSon = nums[:count, RDSon_index].flatten()
    VGS = nums[:count, VGS_index].flatten()

    print(f"IDS: {IDS} \n VDS: {VDS} \n RDSon: {RDSon}")
    

