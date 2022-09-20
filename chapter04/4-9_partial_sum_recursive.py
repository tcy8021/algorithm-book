import random


def func(n: int, w: int, lst: list[int]) -> bool:
    # 0個の要素で作れるのは0だけ
    if n == 0:
        if w == 0:
            return True
        return False

    if func(n - 1, w, lst):
        return True

    if func(n - 1, w - lst[n - 1], lst):
        return True

    return False


def main():
    lst: list[int] = [random.randrange(10) for _ in range(10)]
    target_val: int = random.randrange(50)

    print(f"lst: {lst}")
    print(f"target_val: {target_val}")
    print(func(len(lst), target_val, lst))


if __name__ == "__main__":
    main()
