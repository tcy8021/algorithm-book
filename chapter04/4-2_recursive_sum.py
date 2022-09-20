def recursive_sum(n: int) -> int:
    print(f"recursive_sum({n})を呼び出しました")

    if n == 0:
        return 0

    result: int = n + recursive_sum(n - 1)

    print(f"{n} までの和 = {result}")

    return result


def main():
    recursive_sum(5)


if __name__ == "__main__":
    main()
