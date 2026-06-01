import numpy as np
import mplcursors
import matplotlib.pyplot as plt
import matplotlib.cm as cm


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

    char(count, types, nums)

def char(count, types, nums):
    print(nums)
