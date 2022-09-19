import random


def main():
    LIST_SIZE: int = 1000000
    MAX_VAL: int = 10000000
    target_val: int = random.randrange(MAX_VAL)
    lst: list[int] = [random.randrange(MAX_VAL) for _ in range(LIST_SIZE)]

    # print("lst: ", lst)
    # print("target_val: ", target_val)

    # 線形探索法
    exists: bool = False
    for e in lst:
        if e == target_val:
            exists = True

    if exists:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
