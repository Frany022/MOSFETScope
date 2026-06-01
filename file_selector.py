import tkinter as tk
from tkinter import filedialog

def select_files():
    root = tk.Tk()
    root.withdraw()

    filepath = filedialog.askopenfilename(
        title="Select characterization files",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )

    return filepath

def which_parser(names, DATA_NAME):
    IGS = {
        "IG": "ig",
        "IGabs" : "igabs",
        "VGS" : "vgs"
    }
    Quadrant = {
        "IDS" : "ids",
        "VDS" : "vds"
    }

    for i in range(len(names)):
        names[i] = names[i].replace(DATA_NAME + ", ", "")

    #not the best solution, but works for now
    for i in enumerate(names):
        if i == "Rdson" or "Rdson\n" or "RDSon" or "RDSon\n":
            return "RDSon"
        elif i == "IG" or "IGabs":
            return "IG"
        else:
            return "Quadrant"





