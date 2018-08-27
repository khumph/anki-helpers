import sys
import re
import argparse

parser = argparse.ArgumentParser(
    description="""
    Formats a .md file into .csv files suitable for import into Anki.
    Expects a single letter field indicating note type ('b' for basic,
     'r' for basic (and reversed), 'c' for cloze, and 'o' for cloze (overlapping))
    as the first field followed by front, back, and remarks fields, with each
    field separated by a semicolon and the note ended with '---'.
    """,
    epilog="""
    Also adds tags and sources (same for each note).
    """
)
parser.add_argument("inputfile",
                    help="Markdown file to format",
                    type=argparse.FileType('r'),
                    default=sys.stdin)
parser.add_argument("sources", help = "Text to fill the sources field")
parser.add_argument("tags", help = "Tags (quoted and separated by spaces)")

args = parser.parse_args()

input_file = args.inputfile.read()

out = re.sub(r'\n+', '<br>', input_file)
out = re.sub(r'\s*(<br>)*\s*;\s*(<br>)*\s*', ';', out)
out = re.sub(r'(<br>)*---+(<br>)*',
                     ';{};{}\n'.format(args.sources, args.tags), out)

out = out.splitlines()

output_cards = [[], [], [], []]
for line in out:
    if line[:2] not in ['b;', 'r;', 'c;', 'o;']:
        print(line)
        raise Exception("Card type in above line not specified correctly")
    elif line[0] == "b":
        output_cards[0].append(line[2:])
    elif line[0] == "r":
        output_cards[1].append(line[2:])
    elif line[0] == "c":
        output_cards[2].append(line[2:])
    elif line[0] == "o":
        output_cards[3].append(line[2:])

files = ["basic.csv", "and-reversed.csv", "cloze.csv", "overlapping.csv"]
for cards, file in zip(output_cards, files):
    with open(file, "w") as output_file:
        print("\n".join(cards), file=output_file, end='')
