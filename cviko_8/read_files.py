import sys

fname = sys.argv[1]

f = open(fname, 'r')

for i, line in enumerate(f):
    print(f"Line {i}:", line)

f.close()

