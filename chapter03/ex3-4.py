import random


def main():
    LIST_SIZE: int = 10
    MAX_VAL: int = 100

    lst: list[int] = [random.randrange(MAX_VAL) for _ in range(LIST_SIZE)]
    print("lst:", lst)

    min_val: int = MAX_VAL
    max_val: int = 0
    for e in lst:
        if e < min_val:
            min_val = e

        if e > max_val:
            max_val = e

    print("max_val:", max_val)
    print("min_val:", min_val)
    print(max_val - min_val)


if __name__ == "__main__":
    main()
