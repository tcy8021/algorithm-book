def fib(n: int, memo: list[int]) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if memo[n] != -1:
        return memo[n]

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def main():
    memo: list[int] = [-1] * 100

    fib(99, memo)

    for e in memo:
        print(e)


if __name__ == "__main__":
    main()
