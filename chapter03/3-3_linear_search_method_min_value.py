import random


def main():
    LIST_SIZE: int = 10
    MAX_VAL: int = 100
    lst: list[int] = [random.randrange(MAX_VAL) for _ in range(LIST_SIZE)]

    print("lst: ", lst)

    # 線形探索法
    min_val: int = MAX_VAL
    for e in lst:
        if e < min_val:
            min_val = e

    print(min_val)


if __name__ == "__main__":
    main()
