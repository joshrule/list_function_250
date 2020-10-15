import csv
import json
import os
import os.path
import pandas as pd
import sys

def json2csv(jsonFile):
    with open(jsonFile, 'r') as fd:
        obj = json.load(fd)
    concept = obj["id"]
    program = obj["program"]
    records = [
        {
            "id": concept,
            "program": program,
            "i": datum["i"],
            "o": datum["o"],
        }
        for datum in obj["data"]]
    outFile = os.path.splitext(jsonFile)[0] + ".csv"
    df = pd.DataFrame.from_records(records)
    df.to_csv(outFile, quoting=csv.QUOTE_MINIMAL, index=False)

def json2txt(jsonfile):
    records = []
    with open(jsonfile, 'r') as fd:
        obj = json.load(fd)
    concept = obj["id"]
    program = obj["program"]
    outFile = os.path.splitext(jsonfile)[0] + ".txt"
    with open(outFile, 'w') as fd:
        fd.write("# " + concept + ": " + program + "\n")
        for datum in obj["data"]:
            i_list = ",".join([str(x) for x in datum["i"]])
            o_list = ",".join([str(x) for x in datum["o"]])
            fd.write(i_list + ";" + o_list + "\n")

def usage():
    return (
        "python json2.py <format> <file>\n"
        "    <format>: 'csv' or 'txt'\n"
        "    <file>: the json file" )

if __name__ == "__main__":
    """json2.py
    usage: python json2.py <format> <file>
        <format>: 'csv' or 'txt'
        <file>: the json file"
    """
    # get the arguments
    if len(sys.argv) != 3:
        print(usage())
    else:
        if sys.argv[1] == "csv":
            json2csv(sys.argv[2])
        elif sys.argv[1] == "txt":
            json2txt(sys.argv[2])
        else:
            print(usage())
