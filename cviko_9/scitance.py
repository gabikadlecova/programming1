import sys


def rozklad(N, num_k, min_prev, res):
    if num_k == 1:
        print(f"{res} {N}")
        return

    for i in range(1, N):
        if i > N - i or i < min_prev:
            continue

        next_res = f"{res} {i}"
        rozklad(N - i, num_k - 1, i, next_res)


if __name__ == "__main__":
    rozklad(int(sys.argv[1]), int(sys.argv[2]), 1, "")
