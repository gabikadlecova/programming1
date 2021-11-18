import sys
from write_file import write_to_file


if __name__ == "__main__":
    out_fname = sys.argv[1]
    in_fname = sys.argv[2]

    with open(in_fname, 'r') as in_f:
        lines = [l for l in in_f]

    write_to_file(out_fname, lines)
    print("written")

