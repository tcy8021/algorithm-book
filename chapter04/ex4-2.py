def tribonacci(n: int, memo: list[int]) -> int:
    if n in (0, 1):
        return 0
    elif n == 2:
        return 1

    if memo[n] != -1:
        return memo[n]

    memo[n] = (
        tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo)
    )
    return memo[n]


def main():
    print("n: ", end="")
    n: int = int(input())

    memo: list[int] = [-1] * (n + 1)

    print(tribonacci(n, memo))


if __name__ == "__main__":
    main()
