def main():
    lst: list[int] = [1, 2, 3, 3, 4, 5]
    target_val: int = 3

    count: int = 0
    for e in lst:
        if e == target_val:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
