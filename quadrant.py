import numpy as np
import mplcursors
import matplotlib.pyplot as plt
import matplotlib.cm as cm

for_quadrant = {
    "VDS" : "vds",
    "IDS": "ids",
    "VGS" : "vgs",
    "IDSabs" : "idsabs",
    "VDSabs" : "vdsabs"
}

def char(count: int, types: str, nums: float):

    VDS_index = [i for i, x in enumerate(types) if x.lower() == for_quadrant["VDS"]]
    IDS_index = [i for i, x in enumerate(types) if x.lower() == for_quadrant["IDS"]]
    VGS_index = [i for i, x in enumerate(types) if x.lower() == for_quadrant["VGS"]]
    IDSabs_index = [i for i, x in enumerate(types) if x.lower() == for_quadrant["IDSabs"]]
    VDSabs_index = [i for i, x in enumerate(types) if x.replace("\\n", "").strip().lower() == for_quadrant["VDSabs"]]

    nums = np.array(nums)

    VGS = nums[:count, VGS_index].flatten()
    IDS = nums[:count, IDS_index].flatten()
    VDS = nums[:count, VDS_index].flatten()
    IDSabs = nums[:count, IDSabs_index].flatten()
    VDSabs = nums[:count, VDSabs_index].flatten()

    fig, ax = plt.subplots()
    line_to_data = {}

    VGS_values = np.unique(np.round(VGS, 3))
    colors = cm.viridis(np.linspace(0, 1, len(VGS_values)))

    for vgs, color in zip(VGS_values, colors):
        mask = np.isclose(VGS, vgs)
        idx = np.argsort(VDSabs[mask])

        x = VDSabs[mask][idx]
        y = IDSabs[mask][idx]
        
        line, = ax.plot(x, y, color=color, label=f"Quadrant")
        line_to_data[line] = (x, y, vgs)
    
    ax.legend()
    cursor = mplcursors.cursor(list(line_to_data.keys()), hover=True)

    @cursor.connect("add")
    def on_add(sel):
        line = sel.artist
        i = int(round(sel.index))

        x, y, vgs = line_to_data[line]

        sel.annotation.set_text(f"VGS:{vgs}V")

    plt.title("3rd Quadrant char")
    plt.xlabel("VDSabs (V)")
    plt.ylabel("IDSabs (A)")
    plt.legend()
    plt.show()

