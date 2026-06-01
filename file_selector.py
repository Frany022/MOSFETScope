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

def which_parser(names, DATA_NAME):
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
