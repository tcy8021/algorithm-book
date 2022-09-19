def main():
    lst: list[int] = [1, 2, 4, 5, 11]
    target_val: int = 10

    exists: bool = False
    for bit in range(1 << len(lst)):
        sum: int = 0
        for i, e in enumerate(lst):
            if bit & (1 << i):
                sum += e

        if sum == target_val:
            exists = True

    print(exists)


if __name__ == "__main__":
    main()
