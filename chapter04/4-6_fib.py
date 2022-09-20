def fib(n: int) -> int:
    print(f"fib({n})")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    result: int = fib(n - 1) + fib(n - 2)
    print(f"n = {n}, result = {result}")

    return result


def main():
    fib(6)


if __name__ == "__main__":
    main()
