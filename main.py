import rdson
import igs
import quadrant
import csv
import file_selector

DATA_NAME = "DataName"
DATA_VALUE = "DataValue"


def main():
    data = []
    names = []
    count = 0
    file_name = file_selector.select_files()

    if(file_name):
        print("File found")
    else:
        print("File cannot be found")
    
    with open(file_name, "r") as reader:
        csv_file = csv.reader(file_name, delimiter=',')
        for row in reader:
            if DATA_VALUE in row:
                data.append(row)
                count += 1
            elif DATA_NAME in row:
                data.append(row)
                names.append(row)
            else:
                pass
    reader.close

    types, nums = file_selector.parser(data, DATA_VALUE, DATA_NAME, count)
    which_one = file_selector.which_char(names, DATA_NAME)
    if which_one == "RDSon":
        print("RDSon found, plotting..")
        rdson.char(count, types, nums)
    elif which_one == "IG":
        print("IG found, plotting..")
        igs.char(count, types, nums)
    elif which_one == "Quadrant":
        print("3rd Quadrant found, plotting..")
        quadrant.char(count, types, nums)
    else:
        print("No characterization parameter found, exiting..")


main()
