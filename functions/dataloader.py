from os import listdir
from os.path import isfile, join
import csv
from pprint import pp


def csv2list(csv_file):
    row_dicts = list()
    with open() as csv_file:
        index = 0
        lines = csv.reader(csv_file, delimiter=",")
        for row in lines:
            if index == 0:
                fields = list(row)
            else:
                new_dict = dict()
                for i in range(len(fields)):
                    new_dict[fields[i]] = row[i]
                row_dicts.append(new_dict)
            index += 1
        print(f" lines read : {index}  \n")
    pp(row_dicts)


def list_files(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles
