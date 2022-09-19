import random


def main():
    LIST_SIZE: int = 10
    MAX_VAL: int = 100

    st: set[int] = set([random.randrange(MAX_VAL) for _ in range(LIST_SIZE)])
    print("st:", st)

    min_val: int = MAX_VAL
    second_min_val = MAX_VAL
    for e in st:
        if e < min_val:
            second_min_val = min_val
            min_val = e

        if e > min_val and e < second_min_val:
            second_min_val = e

    print("min_val:", min_val)
    print("second_min_val:", second_min_val)


if __name__ == "__main__":
    main()
