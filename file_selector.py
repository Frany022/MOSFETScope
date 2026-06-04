import tkinter as tk
from tkinter import filedialog

required_names = {
    "RDSon" : {"ids", "vds", "vgs"},
    "IG": {"vgs"},
    "Quadrant" : {"ids", "vds"}
}

rdson_names = {"rdson"}
ig_names = {"ig", "igabs"}

def select_files():
    root = tk.Tk()
    root.withdraw()

    filepath = filedialog.askopenfilename(
        title="Select characterization files",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )

    return filepath

def parser(data, DATA_VALUE: str, DATA_NAME: str, count: int):
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

    return types, nums

def which_char(names, DATA_NAME):
    names = [n.replace(DATA_NAME + ", ", "").replace("\\n", "").strip().lower() for n in names]
    names = ", ".join(names).split(", ")
    names = [n.strip().lower() for n in names]
    normalized = set(names)
    '''
    debug
    print("normalized:", normalized)
    print("rdson check:", required_names["RDSon"].issubset(normalized), any(n in normalized for n in rdson_names))
    print("ig check:", required_names["IG"].issubset(normalized), any(n in normalized for n in ig_names))
    print("quadrant check:", required_names["Quadrant"].issubset(normalized))
    '''
    if required_names["RDSon"].issubset(normalized) and any(n in normalized for n in rdson_names):
        return "RDSon"
    elif required_names["IG"].issubset(normalized) and any(n in normalized for n in ig_names):
        return "IG"
    elif required_names["Quadrant"].issubset(normalized):
        return "Quadrant"
    
    return None
