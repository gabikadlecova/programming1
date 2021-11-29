def fibo(N, from_N):
    print("From: ", from_N)
    print("Current: ", N)
    print()

    if N <= 1:
        return 1

    return fibo(N - 1, N) + fibo(N - 2, N)


if __name__ == "__main__":
    print(fibo(5, 5))
