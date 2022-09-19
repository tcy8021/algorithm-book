import random


def main():
    LIST_SIZE: int = 1000000
    MAX_VAL: int = 10000000
    target_val: int = random.randrange(MAX_VAL)
    lst: list[int] = [random.randrange(MAX_VAL) for _ in range(LIST_SIZE)]

    # print("lst: ", lst)
    # print("target_val: ", target_val)

    # 線形探索法
    idx: int = -1
    for i, e in enumerate(lst):
        if e == target_val:
            idx = i

    print(idx)


if __name__ == "__main__":
    main()
