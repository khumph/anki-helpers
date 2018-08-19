import sys
import re
import argparse

parser = argparse.ArgumentParser(
    description="""
    Creates a list of .csv files that aren't empty and a list of each associated
    card type for import into an applescript which in turn adds them to Anki.
    """
)
parser.add_argument("-f", dest="filenames",
                    help="list of .csv filenames to import (result of find)",
                    type=argparse.FileType('r'),
                    default=sys.stdin)

args = parser.parse_args()

filenames = args.filenames.read()

if filenames == '':
    raise Exception("All input .csv files are empty. Add some notes to input.md and try again.")

filenames = re.sub(r'\./', '', filenames).split()

types = []
for filename in filenames:
    if filename == "basic.csv":
        types.append("Basic")
    elif filename == "and-reversed.csv":
        types.append("Basic (and reversed card)")
    elif filename == "overlapping.csv":
        types.append("Cloze (overlapping)")
    elif filename == "cloze.csv":
        types.append("Cloze")

# {"basic.csv", "and-reversed.csv", "overlapping.csv", "cloze.csv"}
# {"Basic", "Basic (and reversed card)", "Cloze (overlapping)", "Cloze"}
filenames = "'{\"" + '", "'.join(filenames) + "\"}'"
types = "'{\"" + '", "'.join(types) + "\"}'"

print(filenames, types, file=sys.stdout)
