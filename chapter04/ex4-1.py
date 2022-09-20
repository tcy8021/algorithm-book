def tribonacci(n: int) -> int:
    if n in (0, 1):
        return 0
    elif n == 2:
        return 1

    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


def main():
    print("n: ", end="")
    n: int = int(input())

    print(tribonacci(n))


if __name__ == "__main__":
    main()
