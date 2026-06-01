import numpy as np
import mplcursors
import matplotlib.pyplot as plt
import matplotlib.cm as cm

for_rdson = {
    "IDS" : "IDS",
    "VDS" : "VDS",
    "VGS" : "VGS"
}

def parser(data, DATA_VALUE, DATA_NAME, count):
    for i in range(len(DATA_NAME)):
        types = data[0].replace(DATA_NAME + "," + " ", "")
        types = types.split(", ")
    nums = [[0 for i in range(len(types))] for j in range(count)]
    for i in range(count + 1):
        if i == 0:
            continue
        values = data[i].replace(DATA_VALUE + "," + " ", "")
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
    RDSon_index = [i for i, x in enumerate(types) if x in ("Rdson", "Rdson\n", "RDSon", "RDSon\n")]
    VGS_index = [i for i, x in enumerate(types) if x == for_rdson["VGS"]]

    if not IDS_index:   print("No IDS for char");   return
    if not VDS_index:   print("No VDS for char");   return
    if not RDSon_index: print("No rdson for char"); return
    if not VGS_index:   print("No vgs for char");   return

    nums = np.array(nums)

    IDS = nums[:count, IDS_index[0]].flatten()
    VDS = nums[:count, VDS_index[0]].flatten()
    RDSon = nums[:count, RDSon_index[0]].flatten()
    VGS = nums[:count, VGS_index[0]].flatten()
    VGS_values = np.unique(np.round(VGS, 3))
    #print(f"IDS: {IDS} \n VDS: {VDS} \n RDSon: {RDSon}")

    colors = cm.viridis(np.linspace(0, 1, len(VGS_values)))

    fig, ax = plt.subplots()

    line_to_data = {}

    for vgs, color in zip(VGS_values, colors):
        mask = np.isclose(VGS, vgs)
        idx = np.argsort(VDS[mask])

        x = VDS[mask][idx]
        y = IDS[mask][idx]
        r = RDSon[mask][idx]

        line, = ax.plot(x, y, color=color, label=f"VGS = {vgs}V")

        line_to_data[line] = (x, y, r, vgs)
    
    ax.legend()

    cursor = mplcursors.cursor(hover=True)

    @cursor.connect("add")
    def on_add(sel):
        line = sel.artist
        i = int(sel.index)

        x, y, r, vgs = line_to_data[line]

        sel.annotation.set_text(f"RDSon:{r[i]:.7f} ohm " f"VGS={vgs}V")

    plt.title("Normal Output Char")
    plt.xlabel("VDS (V)")
    plt.ylabel("IDS (A)")
    plt.legend()
    plt.show()
    

