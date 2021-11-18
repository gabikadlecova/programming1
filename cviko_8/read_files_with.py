import sys

fname = sys.argv[1]

with open(fname, 'r') as f:
    for i, line in enumerate(f):
        print(f"Line {i}:", line)

