import numpy as np
import mplcursors
import matplotlib.cm as cm
import matplotlib.pyplot as plt

for_igs = {
    "VDS" : "vds",
    "IG" : "ig",
    "VGS" : "vgs",
    "IGabs" : "igabs"
}

def char(count: int, types: str, nums: float):

    VDS_index = [i for i, x in enumerate(types) if x.lower() == for_igs["VDS"]]
    IG_index = [i for i, x in enumerate(types) if x.lower() == for_igs["IG"]]
    VGS_index = [i for i, x in enumerate(types) if x.lower() == for_igs["VGS"]]
    IGabs_index = [i for i, x in enumerate(types) if x.replace("\\n", "").strip().lower() == for_igs["IGabs"]]

    if not VDS_index: print("No VDS for char"); return
    if not IG_index: print("No IG for char"); return
    if not VGS_index: print("No VGS for char"); return
    if not IGabs_index : print("No IGabs for char"); return

    nums = np.array(nums)

    VDS = nums[:count, VDS_index].flatten()
    IG = nums[:count, IG_index].flatten()
    VGS = nums[:count, VGS_index].flatten()
    IGabs = nums[:count, IGabs_index].flatten()
    
    #print(f"VDS: {VDS} \nIG: {IG}\nVGS: {VGS}\nIGabs: {IGabs}")

    fig, ax = plt.subplots()
    line_to_data = {}

    VDS_values = np.unique(np.round(VDS, 3))
    colors = cm.viridis(np.linspace(0, 1, len(VDS_values)))

    for vds, color in zip(VDS_values, colors):
        mask = np.isclose(VDS, vds)
        idx = np.argsort(VGS[mask])
        x = VGS[mask][idx]
        y = IG[mask][idx]
        igabs = IGabs[mask][idx]
        line, = ax.plot(x, y, color=color, label=f"VDS={vds}V")

        line_to_data[line] = (x, y, igabs, vds)
    
    ax.legend()

    cursor = mplcursors.cursor(list(line_to_data.keys()), hover=True)

    @cursor.connect("add")
    def on_add(sel):
        line = sel.artist
        i = int(round(sel.index))

        x, y, iagbs, vds = line_to_data[line]

        sel.annotation.set_text(f"IGabs={igabs[i]:.3e}")

    plt.title("IG char")
    plt.xlabel("VGS (V)")
    plt.ylabel("IG (A)")
    plt.legend()
    plt.show()
