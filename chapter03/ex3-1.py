def main():
    lst: list[int] = [1, 1, 1, 1, 1]
    target_val: int = 1

    idx: int = -1
    for i, e in enumerate(lst):
        if e == target_val:
            idx = i

    print(idx)


if __name__ == "__main__":
    main()
