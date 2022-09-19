import sys


def main():
    lst1: list[int] = [8, 5, 4]
    lst2: list[int] = [4, 1, 9]
    target_val: int = 10

    min_val: int = sys.maxsize
    print(min_val)

    for a in lst1:
        for b in lst2:
            if a + b >= target_val and a + b < min_val:
                min_val = a + b

    print(min_val)


if __name__ == "__main__":
    main()
