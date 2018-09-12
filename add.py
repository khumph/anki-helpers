#!/usr/bin/env python3

import sys
import re
import argparse
import requests

parser = argparse.ArgumentParser(
    description="""
    Formats an .md file for import into Anki, then imports each note from the 
    file into Anki using AnkiConnect.
    Expects a single letter field indicating note type ('b' for basic,
     'r' for basic (and reversed), 'c' for cloze, and 'o' for cloze (overlapping))
    as the first field followed by front, back, remarks, sources, and tags 
    fields, with each field separated by a semicolon and the note ended with '---'.
    """
)
parser.add_argument("inputfile",
                    help="Markdown file with notes to add to Anki",
                    type=argparse.FileType('r'),
                    default=sys.stdin)

args = parser.parse_args()

input_file = args.inputfile.read()

out = re.sub(r'\n+', '<br>', input_file)
out = re.sub(r'\s*(<br>)*\s*;\s*(<br>)*\s*', ';', out)
out = re.sub(r'(<br>)*---+(<br>)*', '\n', out)

out = out.splitlines()

for line in out:
    data = '''{{
        "action": "addNote",
        "version": 6,
        "params": {{
            "note":
                {{
                "deckName": "new",
                "modelName": "{}",
                "fields": {{
                    "Front": "{}",
                    "Back": "{}",
                    "Remarks": "{}",
                    "Sources": "{}"
                }},
                "tags": ["{}"]
            }}
        }}
    }}'''

    args = line.split(";")

    if args[0] not in ['b', 'r', 'c', 'o']:
        print(line)
        raise Exception("Card type in above line not specified correctly")
    elif args[0] == "b":
        args[0] = "Basic"
    elif args[0] == "r":
        args[0] = "Basic (and reversed card)"
    elif args[0] == "c":
        args[0] = "Cloze"
        data = re.sub('Front', 'Text', data)
        data_split = data.splitlines()
        data_split.remove('                    "Back": "{}",')
        data = '\n'.join(data_split)
    elif args[0] == "o":
        args[0] = "Cloze (overlapping)"
        data = re.sub('Front', 'Title', data)
        data = re.sub('Back', 'Original', data)
    
    data = data.format(*args)

    r = requests.post('http://localhost:8765', data=data)

    print(line)
    print(r.text + "\n")
