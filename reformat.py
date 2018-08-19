import sys
import re
import argparse

parser = argparse.ArgumentParser(
    description="""
    Reformats input text file into MathJax math syntax with appropriate spacing
    and capitalizes each line.
    """
)
parser.add_argument("-f", "--file", dest="inputfile",
                    help="reformat FILE (instead of stdin)",
                    type=argparse.FileType('r'),
                    metavar="FILE",
                    default=sys.stdin)

args = parser.parse_args()

input_file = args.inputfile.read()

out = re.sub(r'\[latex\]\s*', '', input_file)
out = re.sub(r'\s*\[/latex\]', '', out)
out = re.sub(r'\[\$\]', '\(', out)
out = re.sub(r'\[/\$\]', '\)', out)
out = re.sub(r'\[\$\$\]', '\[', out)
out = re.sub(r'\[/\$\$\]', '\]', out)
# unfortunately the $$ syntax doesn't allow easy reformatting:
out = re.sub(r'\$', '\(', out)
out = re.sub(r'\$\$', '\[ ', out)
out = re.sub(r'\\\(\s*', '\(', out)
out = re.sub(r'\s*\\\)', '\)', out)
out = re.sub(r'\\\[\s*', '\[ ', out)
out = re.sub(r'\s*\\\]', ' \]', out)
out = "\n".join([line[0].upper() + line[1:] for line in out.split("\n")]) + "\n"

sys.stdout.write(out)
 