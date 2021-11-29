import sys


def subseq(start, N_max, seq_len, res):
    if seq_len == 0:
        print(res)
        return

    for i in range(start, N_max):
        next_res = res + f"{i + 1}"

        subseq(i + 1, N_max, seq_len - 1, next_res)


print('neco')


if __name__ == "__main__":
    #max_n = 3
    max_n = int(sys.argv[1])
    print(sys.argv)

    for i in range(max_n):
        subseq(0, max_n, i + 1, "")
