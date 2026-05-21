import csv
import rdson
import igs
import quadrant
import numpy as np
import matplotlib as mpl


def main():
    data, count = rdson.read_csv()
    print(f"{data}")

main()
